import subprocess
from scapy.all import *

def get_interfaces():
    """Lấy danh sách các giao diện mạng."""
    try:
        result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
        if result.returncode == 0:  # Kiểm tra mã trả về
            output_lines = result.stdout.splitlines()[3:]
            interfaces = [line.split()[3] for line in output_lines if len(line.split()) >= 4]
            return interfaces
        else:
            print(f"Lỗi khi chạy netsh: {result.stderr}")
            return []  # Trả về danh sách rỗng nếu có lỗi
    except FileNotFoundError:
        print("Lệnh netsh không tìm thấy.")
        return []  # Trả về danh sách rỗng nếu netsh không tìm thấy
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return []  # Trả về danh sách rỗng nếu có lỗi không xác định

def packet_handler(packet):
    """Xử lý gói tin mạng."""
    if packet.haslayer(Raw):
        print("Captured Packet:")
        print(str(packet))

interfaces = get_interfaces()

if not interfaces:  # Kiểm tra danh sách giao diện mạng rỗng
    print("Không tìm thấy giao diện mạng nào.")
else:
    print("Danh sách các giao diện mạng:")
    for i, iface in enumerate(interfaces, start=1):
        print(f"{i}. {iface}")

    try:
        choice = int(input("Chọn một giao diện mạng (nhập số): "))
        selected_iface = interfaces[choice - 1]

        sniff(iface=selected_iface, prn=packet_handler, filter="tcp")
    except ValueError:
        print("Vui lòng nhập một số nguyên.")
    except IndexError:
        print("Lựa chọn không hợp lệ.")