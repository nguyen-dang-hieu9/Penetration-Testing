# **Khái niệm:**

Leo thang đặc quyền liên quan đến việc chuyển từ 1 tài khoản có đặc quyền thấp sang tài khoản có đặc quyền cao hơn. Nói về kĩ thuật, nó là khai thác 1 lỗ hổng, lỗi thiết kế hay giám sát cấu hình trong hệ điều hành hay ứng dụng để truy cập trái phép những tài nguyên bị giới hạn xem bởi người dùng.

Tại sao nó quan trọng?

Rất hiếm khi kiểm thử xâm nhập có thể giành được foothold (initial access) mà cho bạn trực tiếp truy cập quyền quản trị viên. Leo thang đặc quyền rất nghiêm trọng vì nó cho phép bạn dành được quyền quản trị hệ thống để thực hiện những hành động sau:

* Đặt lại mật khẩu
    
* Bỏ qua kiểm soát truy cập để thâm nhập dữ liệu được bảo vệ
    
* Chỉnh sửa cấu hình phần mềm
    
* Thay đổi đặc quyền của người dùng đang tồn tại
    
* Thực thi các lệnh của quản trị viên
    

# **Enumeration** 

Liệt kê là bước đầu tiên bạn phải làm để giành được quyền truy cập vào hệ thống. Bạn có thể truy cập hệ thống bằng việc khai thác 1 lỗ hổng nghiêm trọng dẫn đến quyền root hoặc chỉ tìm được cách để gửi các lệnh bằng tài khoản có đặc quyền thấp.

Trong bản cam kết kiểm thử thâm nhập, không như ctf, sẽ không kết thúc cho đến khi bạn dành được quyền truy cập vào 1 hệ thống xác định hay người dùng có đặc quyền cao. Như bạn có thể thấy, liệt kê là 1 bước rất quan trọng trước khi bắt đầu thâm nhập 1 hệ thống. 

## **hostname**

Lệnh hostname sẽ trả về tên máy chủ của máy đích. Mặc dù giá trị này có thể dễ dàng thay đổi hoặc là 1 chuỗi vô giá trị như Ubuntu-3487340239, trong một vài trường hợp, nó có thể cung cấp thông tin về vai trò của hệ thống đích trong 1 mạng doanh nghiệp (e.g. SQL-PROD-01 for a production SQL server).

## **uname -a**

Sẽ in thông tin hệ thống cho chúng ta thêm thông tin về nhân được dùng bởi hệ thống. Điều này sẽ rất hữu ích khi tìm kiếm các lỗ hổng liên quan đến nhân có thể dẫn đến sự leo thang đặc quyền.

## **/proc/version**

Hệ thống tệp proc cung cấp thông tin về các processes của hệ thống đích. Bạn sẽ tìm thấy proc trên rất nhiều bản phân phối của Linux, biến nó trở thành 1 công cụ rất cần thiết để có trong bộ vũ khí của bạn.

Tìm kiếm /proc/version có thể cho bạn thông tin về phiên bản của nhân và các trình biên dịch đã được cài đặt (ví dụ: GCC)

## **/etc/issue**

Các hệ thống có thể được định danh trong tệp /etc/issue. Tệp này chứa một vài thông tin về hệ điều hành nhưng dễ bị điều chỉnh hay thay đổi.

Bất cứ tệp nào chứa thông tin về hệ thống đều có thể bị điều chỉnh. Để hiểu rõ hơn về hệ thống, vẫn tốt hơn là xem hết chúng.

## **Lệnh ps** 

Lệnh ps là 1 cách hiệu quả để xem các quá trình đang chạy trên hệ thống Linux.

Đầu ra của ps sẽ hiện ra như sau:

* PID: ID của process (độc nhất)
    
* TTY: loại terminal được dùng bởi người dùng
    
* Time: Thời gian CPU được dùng bởi process (không phải là thời gian quá trình này đang chạy)
    
* CMD: lệnh hay thực thi đang chạy (sẽ không hiển thị tham số của lệnh)
    

Lệnh ps cung cấp 1 số lựa chọn sau:

* ps -A: xem tất cả processes đang chạy
    
* ps axjf: xem cây process
    

ps aux: aux sẽ hiển thị các processes cho tất cả người dùng, hiển thị người dùng đang chạy process đó (u) và hiển thị các processes không attacked với terminal (x). Nhìn vào đầu ra của lệnh ps aux, chúng ta có thể hiểu rõ hơn về hệ thống và các lỗ hổng tiềm tàng.

## **env**

Lệnh env sẽ hiển thị các biến môi trường.

Biến PATH có thể có 1 trình biên dịch hay 1 ngôn ngữ scripting như Python có thể được dùng để chạy code trên hệ thống đích hoặc tận dụng để leo thang đặc quyền 

## **sudo -l**

Hệ thống đích có thể được cấu hình cho phép người dùng chạy một vài lệnh với quyền root. Lệnh sudo -l có thể được dùng để liệt kê tất cả các lệnh người dùng có thể chạy dưới quyền root.

## **ls**

Một trong những lệnh phổ biến nhất trong Linux có lẽ là ls

## **id**

Lệnh id sẽ cung cấp 1 cái nhìn chung về cấp độ đặc quyền  và tư cách thành viên nhóm của người dùng.

Điều đáng ghi nhớ là lệnh id cũng có thể nhận được thông tin của người dùng khác 

## **/etc/passwd**

Đọc tệp /etc/passwd có thể là 1 cách dễ để khám phá các người dùng trên hệ thống  

## **history**

Nhìn các câu lệnh gần đây với history có thể cho chúng ta một vài ý tưởng về hệ thống đích, đôi khi có lưu trữ thông tin như mật khẩu hay tên người dùng.

## **ifconfig**

Hệ thống đích có thể là 1 điểm pivot đến 1 mạng khác. Lệnh ifconfig sẽ cho chúng ta thông tin về giao diện mạng của hệ thống. Ví dụ dưới có 3 giao diện (eth0, tun0, tun1). Hệ thống đích có thể chạm đến giao diện eth0 nhưng không thể truy cập trực tiếp đến 2 mạng khác. 

## **netstat**

Sau khi kiểm tra các giao diện và tuyến mạng đang tồn tại, rất đáng để xem các kết nối mạng. Lệnh netstat có thể giám sát các kết nối mạng trong toàn hệ thống.

## **Lệnh find**

Tìm kiếm tệp:

* find . -name flag1.txt: tìm kiếm file tên flag1.txt trong thư mục hiện tại
    
* find /home -name flag1.txt: tìm kiếm file trong thư mục /home
    
* find / -type d -name config: tìm kiếm thư mục tên config trong /
    
* find / -type f -perm 0777: tìm kiếm tập tin với permissions là 777
    
* find / -perm a=x: tìm kiếm các file thực thi
    
* find /home -user frank: tìm kiếm tất cả tệp của người dùng frank trong thư mục /home
    
* find / -mtime 10: tìm kiếm tệp được điều chỉnh trong 10 ngày gần đây
    
* find / -atime 10: tìm kiếm tệp được truy cập trong 10 ngày gần đây
    
* find / -cmin -60: tìm kiếm tệp được thay đổi trong vòng 1 giờ qua
    
* find / -amin -60: tìm kiếm tệp được truy cập trong vòng 1 giờ qua
    
* find / -size 50M: tìm kiếm tệp với kích thước 50MB
    

Lệnh find thường tạo ra các lỗi làm cho đầu ra khó đọc. Đó là lí do tại sao phải sử dụng lệnh find với “-type f 2&gt;/dev/null” để chuyển hướng các lỗi đến “/dev/null” và có đầu ra rõ ràng hơn.

Các thư mục và tệp có thể được ghi hoặc thực thi từ:

* find / -writable -type d 2&gt;/dev/null : Find world-writeable folders
    
* find / -perm -222 -type d 2&gt;/dev/null: Find world-writeable folders
    
* find / -perm -o w -type d 2&gt;/dev/null: Find world-writeable folders 
    

# **Leo thang đặc quyền: Khai thác nhân** 

Leo thang đặc quyền tốt nhất là phải lấy được đặc quyền root. Điều này có thể được làm bằng cách khai thác 1 lỗ hổng đã tồn tại, hoặc truy cập tài khoản khác có nhiều đặc quyền hơn.

Nếu lỗ hổng không dẫn đến root shell, quá trình leo thang đặc quyền sẽ dựa vào việc cấu hình sai và quyền hạn lỏng lẻo.

Nhân trong các hệ thống Linux quản lí giao tiếp giữa các thành phần như bộ nhớ trên hệ thống và ứng dụng. Chức năng này yêu cầu nhân có các đặc quyền xác định; do đó 1 khai thác thành công sẽ có thể dẫn đến đặc quyền của root.

Phương pháp khai thác nhân rất đơn giản:

* Xác định phiên bản của nhân
    
* Tìm kiếm mã khai thác đối với nhân của hệ thống đích
    
* Chạy khai thác
    

Mặc dù rất đơn giản,  khai thác nhân bị lỗi có thể làm hệ thống bị hỏng.

Nghiên cứu các mã nguồn:

* Bạn có thể dùng Google để tìm kiếm mã khai thác
    
* Những mã nguồn như [https://www.linuxkernelcves.com/cves](https://www.linuxkernelcves.com/cves) có thể rất hữu ích
    
* Dùng 1 tập lệnh như LES (Linux Exploit Suggester) nhưng nhớ là các công cụ này có thể tạo ra false positives (báo cáo lỗ hổng nhân không ảnh hưởng đến hệ thống đích) hoặc false negatives (không báo cáo bất cứ lỗ hổng nhân nào mặc dù nhân bị lỗ hổng)
    

Bạn có thể vận chuyển mã khai thác từ máy cục bộ sang hệ thống đích bằng SimpleHTTPServer của Python và lệnh wget.

# **Leo thang đặc quyền : Sudo** 

Lệnh sudo mặc định cho phép bạn chạy 1 chương trình với đặc quyền root. Dưới 1 số điều kiện, các nhà quản trị hệ thống có thể cần cung cấp cho người dùng thông thường 1 số đặc quyền linh hoạt. Ví dụ, 1 nhà phân tích SOC có thể cần dùng Nmap thường xuyên nhưng không được quyền truy cập root đầy đủ. Trong tình huống đó, quản trị hệ thống có thể cho phép người dùng này chỉ chạy Nmap với đặc quyền root trong khi vẫn giữ đặc quyền của mình trong phần còn lại của hệ thống.

Bất cứ người dùng nào cũng có thể kiểm tra các vấn đề liên quan đến đặc quyền root bằng lệnh sudo -l 

## **Tận dụng các chức năng của ứng dụng**

Một vài ứng dụng sẽ không có các khai thác có sẵn. Ví dụ, bạn có thể thấy máy chủ Apache2.

Trong trường hợp đó, chúng ta có thể dùng “hack” để rò rỉ thông tin tận dụng chức năng của ứng dụng. Như bạn có thể thấy, Apache2 có 1 lựa chọn hỗ trợ tải các tệp cấu hình thay thế (-f: chỉ định 1 ServerConfigFile thay thế).

Tải tệp /etc/shadow bằng lựa chọn này sẽ dẫn đến thông báo lỗi mà chứa dòng đầu tiên của tệp /etc/shadow

## **Tận dụng LD\_PRELOAD**

Trên một vài hệ thống, bạn có thể thấy lựa chọn môi trường LD\_PRELOAD.

LD\_PRELOAD là 1 chức năng cho phép bất cứ chương trình nào sử dụng thư viện shared. Bài viết này sẽ cho bạn 1 ý tưởng về khả năng của LD\_PRELOAD. Nếu lựa chọn “env\_keep” được thực thi chúng ta có thể tạo 1 thư viện shared sẽ được tải và thực thi trước khi chương trình chạy. Lưu ý là lựa chọn LD\_PRELOAD sẽ bị bỏ qua nếu real user ID khác với effective user ID.

Các bước để leo thang đặc quyền như sau:

1. Kiểm tra LD\_PRELOAD (với lựa chọn env\_keep option)
    
2. Chạy 1 code C đơn giản được biên dịch như 1 tệp share object (.so)
    
3. Chạy chương trình với sudo và LD\_PRELOAD trỏ vào tệp .so của chúng ta
    

Code C sẽ đơn giản sinh ra 1 root shell và có thể được viết như sau:

```javascript
#include <stdio.h>

#include <sys/types.h>

#include <stdlib.h>

 

void _init() {

unsetenv("LD_PRELOAD");

setgid(0);

setuid(0);

system("/bin/bash");

} 
```

Chúng ta có thể lưu code này là shell.c và biên dịch nó bằng gcc thành 1 tệp shared object bằng những tham số sau:

```javascript
gcc -fPIC -shared -o shell.so shell.c -nostartfiles 
```

Bây giờ chúng ta có thể dùng tệp shared object này khi chạy bất cứ chương trình nào bằng lệnh sudo. Trong trường hợp này là Apache2, find ,...

Chúng ta có thể chạy chương trình bằng cách chỉ định lựa chọn LD\_PRELOAD như sau:

```javascript
sudo LD_PRELOAD=/home/user/ldpreload/shell.so find
```

Nó sẽ dẫn đến 1 shell với đặc quyền của root.

# **Leo thang đặc quyền: SUID**

Rất nhiều đặc quyền của Linux kiểm soát dựa trên việc kiểm soát người dùng và sự tương tác tệp. Điều này được làm với permissions. Cho đến bây giờ bạn biết các tệp có thể đọc, ghi và thực thi. Điều này thay đổi với SUID (Set-user Identification) và SGID (Set-group Identification). Chúng cho phép các tệp được thực thi với mức độ đặc quyền của chủ sở hữu tệp tương ứng.

Bạn sẽ chú ý những tệp này có bit ‘s’  sẽ hiển thị mức độ đặc quyền đặc biệt.

```javascript
find / -type f -perm -04000 -ls 2>/dev/null sẽ liệt kê các tệp có SUID hay SGID.
```

Một cách thực hành tốt sẽ là so sánh các tệp thực thi trên danh sách đó với GTFOBins. Chọn SUID sẽ lọc các tệp nhị phân có thể khai thác (bạn có thể dùng đường dẫn này để lọc trước https://gtfobins.github.io/#+suid)

Danh sách trên cho thấy nano có SUID bit set. Không may mắn, GFTObins không cho chúng ta có 1 chiến thắng dễ dàng. Trong thực tế, chúng ta sẽ cần tìm các bước trung gian giúp chúng ta tận dụng được các phát hiện nhỏ.

SUID bit set cho trình soạn thảo văn bản nano cho phép chúng ta tạo, chỉnh sửa và đọc các tệp bằng việc sử dụng đặc quyền của chủ sở hữu tệp. Nano được làm chủ bởi root, đồng nghĩa với việc chúng ta có thể đọc và chỉnh sửa tệp ở đặc quyền cao hơn người dùng bình thường. Ở bước này, chúng ta có hai lựa chọn cơ bản để leo thang đặc quyền: đọc /etc/shadow hay thêm người dùng vào /etc/passwd

Đọc tệp /etc/shadow

nano /etc/shadow sẽ in nội dung của tệp /etc/shadow. Chúng ta có thể dùng công cụ unshadow để tạo 1 tệp có thể crack bởi John the Ripper. Để làm được điều đó, unshadow cần cả hai tệp /etc/shadow và /etc/passwd.

 Việc sử dụng unshadow có thể được dùng như sau:

```javascript
unshadow passwd.txt shadow.txt > passwords.txt 
```

Với wordlist đúng và 1 chút may mắn, John the Ripper có thể trả về 1 hoặc vài mật khẩu ở văn bản rõ ràng.

Một lựa chọn khác là thêm người dùng mới có đặc quyền root. Chúng ta sẽ  không phải bẻ khóa mật khẩu tẻ nhạt.

Chúng ta cần hash của mật khẩu. Điều này có thể được làm nhanh chóng bằng công cụ openssl trong Kali Linux.

Sau đó thêm mật khẩu đó với 1 username trong file /etc/passwd

Khi người dùng được thêm vào (root:/bin/bash được dùng để cung cấp root shell), chúng ta sẽ cần chuyển sang người dùng này và hi vọng sẽ có đặc quyền root.

Khi người dùng được thêm vào (root:/bin/bash được dùng để cung cấp root shell), chúng ta sẽ cần chuyển sang người dùng này và hi vọng sẽ có đặc quyền root. 

# **Leo thang đặc quyền: Capabilities**

Một phương thức khác mà các nhà quản trị hệ thống có thể dùng để tăng mức độ đặc quyền của 1 process hay binary là Capabilities. Capabilities giúp quản lí các đặc quyền ở 1 mức độ chi tiết hơn. Ví dụ, nếu nhà phân tích SOC cần dùng 1 công cụ cần khởi tạo kết nối socket, 1 người dùng bình thường sẽ không thể làm điều đó. Nếu nhà quản trị hệ thống không muốn đưa người dùng đó đặc quyền cao hơn, họ có thể thay đổi capabilities của binary. Kết quả là binary có thể hoàn thành nhiệm vụ mà không cần người dùng có đặc quyền cao.

Chúng ta có thể dùng công cụ getcap để liệt kê các capabilities đã được thực thi. 

Khi chạy với tư cách là người dùng không có đặc quyền, getcap -r / sẽ tạo ra rất nhiều lỗi, vì vậy cách tốt nhất là chuyển đến /dev/null.

Lưu ý là vim và bản sao chép của nó không có SUID bit set. Cách leo thang đặc quyền này sẽ không khả thi khi liệt kê tìm kiếm các tệp có SUID.

GTFObins có 1 danh sách tốt các binaries có thể được tận dụng để leo thang đặc quyền nếu chúng ta thấy bất cứ capabilities nào.

Chúng ta để ý là vim có thể được dùng với lệnh và payload sau: 

Điều này sẽ khởi động 1 root shell:

# **Leo thang đặc quyền: Cron jobs**

Cron jobs được dùng để chạy script hay file nhị phân ở thời gian xác định. Chúng sẽ chạy mặc định với đặc quyền của chủ sở hữu chứ không phải là người dùng hiện tại. Cron jobs được cấu hình thích hợp sẽ không phải là lỗ hổng nhưng chúng có thể leo thang đặc quyền với một vài điều kiện. Ý tưởng khá đơn giản; Nếu có 1 nhiệm vụ đã được lên lịch sẵn với đặc quyền của root và chúng ta có thể thay đổi tập lệnh nó sẽ chạy, sau đó script sẽ chạy với đặc quyền của root.

Các cấu hình của cronjobs được lưu trong crontab (cron tables) để xem thời gian nhiệm vụ sẽ chạy. 

Mỗi người dùng trên hệ thống có tệp crontab và có thể chạy các nhiệm vụ xác định khi họ đang đăng nhập hoặc không. Mục đích của chúng ta sẽ tìm 1 cron job set bởi root và chạy tập lệnh của chúng ta.

Bất cứ người dùng nào cũng có thể đọc cron jobs ở /etc/crontab

Trong khi ctf có thể có cron jobs chạy mỗi phút hay mỗi 5 phút, bạn sẽ thường thấy các nhiệm vụ chạy hằng ngày, hàng tuần trong cam kết kiểm thử.

Bạn có thể thấy tập lệnh backup.sh được cấu hình để chạy mỗi phút. Nội dung của tệp là 1 tập lệnh đơn giản mà tạo 1 bản sao lưu của tệp prices.xls

Vì người dùng thường có thể truy cập tập lệnh này, chúng ta dễ dàng điều chỉnh nó để tạo 1 reverse shell, mong muốn có đặc quyền root.

Tập lệnh sẽ sử dụng các công cụ trên hệ thống đích để khởi động 1 reverse shell.

Hai điểm lưu ý là:

* Cú pháp lệnh sẽ khác nhau dựa vào các công cụ (Ví dụ, nc sẽ không hỗ trợ flag -e mà bạn có thể dùng trong nhiều trường hợp)
    
* Chúng ta thích bắt đầu reverse shell vì chúng ta không muốn thâm nhập tính toàn vẹn của hệ thống trong cam kết kiểm thử.
    

Tệp nên giống như sau:

Chúng ta sẽ chạy 1 listener ở máy tấn công để nhận kết nối đang đến.

Crontab rất đáng để kiểm tra vì nó dễ dẫn đến leo thang đặc quyền. Kịch bản sau đây không phải là hiếm gặp ở các công ty mà bảo mật không tốt:

1. Các nhà quản trị hệ thống cần chạy 1 tập lệnh theo định kỳ
    
2. Họ có thể tạo 1 cron job để làm điều đó
    
3. Sau một thời gian, tập lệnh trở nên vô ích và họ xóa nó
    
4. Họ không dọn sạch cron job có liên quan
    

 Ví dụ trên cho thấy 1 tình huống tương tự  nơi mà tập lệnh antivirus.sh đã được xóa nhưng cron job vẫn tồn tại. Nếu đường dẫn đầy đủ của tập lệnh này không được khai báo như backup.sh, cron sẽ tham chiếu đến các đường dẫn được liệt kê dưới biến PATH trong /etc/crontab. Trong trường hợp đó, chúng ta có thể tạo 1 script tên antivirus.sh trong thư mục home/user và nó sẽ chạy như cron job.

Tệp trên hệ thống đích có nội dung như sau: 

Kết nối reverse shell sẽ có đặc quyền root: 

Nếu bạn tìm thấy 1 tập lệnh hay nhiệm vụ trong cronjob, nó rất đáng để dành thời gian hiểu chức năng của tập lệnh và cách các công cụ có thể được dùng trong bối cảnh đó. Ví dụ, tar, 7z, rsync, etc,… có thể được khai thác bằng tính năng wildcard.

# **Leo thang đặc quyền: PATH**

Nếu 1 thư mục mà người dùng của bạn có đặc quyền ghi trong đường dẫn, bạn có thể chiếm quyền điều khiển 1 ứng dụng để chạy tập lệnh. PATH trong Linux là 1 biến môi trường cho hệ điều hành biết nơi để tìm kiếm các tệp thực thi. Bất cứ lệnh nào không được dựng sẵn trong shell hay không khai báo 1 đường dẫn rõ ràng, Linux sẽ bắt đầu tìm kiếm các thư mục được khai báo trong PATH.

PATH sẽ có dạng như sau:

Nếu chúng ta đánh lệnh thm, đó là các vị trí mà Linux sẽ tìm các file thực thi gọi là thm. Diễn cảnh bên dưới sẽ cho chúng ta 1 ý tưởng về cách nó được tận dụng để gia tăng mức độ đặc quyền. Điều này phụ thuộc hoàn toàn vào cấu hình đang có của hệ thống đích, vì vậy phải đảm bảo bạn có thể trả lời các câu hỏi sau trước khi thử nó:

1.Các thư mục được đặt ở $PATH

2.Người dùng hiện tại của bạn có đặc quyền ghi cho thư mục trong đó không

3.Bạn có thể điều chỉnh $PATH

4.Có 1 ứng dụng hay tập lệnh nào sẽ bị ảnh hưởng bởi lỗ hổng này?

Để demo, chúng ta sẽ dùng tập lệnh bên dưới:

Tập lệnh này cố gắng khởi động 1 tệp nhị phân trong hệ thống gọi là thm nhưng ví dụ này có thể dễ dàng bị lặp lại với nhị phân khác.

Chúng ta biên dịch nó thành 1 tệp thực thi và đặt SUID bit.

Người dùng bây giờ có thể truy cập tập lệnh path với SUID bit.

Khi path được thực thi sẽ tìm kiếm tệp thực thi gọi là thm trong các thư mục của PATH.

Nếu bất cứ thư mục nào có thể ghi trong PATH chúng ta có thể tạo 1 tệp nhị phân tên là thm và có tập lệnh trong đó. Vì SUID bit đã được set, tệp nhị phân này sẽ chạy với đặc quyền của root.

Tìm kiếm thư mục có thể ghi bằng lệnh sau:

```javascript
find / -writable 2>/dev/null 
```

Đầu ra của lệnh có thể được dọn sạch bằng lệnh cut và sort đơn giản.

Một vài ctf có thể hiển thị các thư mục khác nhau nhưng 1 hệ thống thường sẽ in ra các thứ chúng ta nhìn thấy ở trên. 

So sánh nó với PATH :

Chúng ta thấy một vài folder trong /usr, do đó có thể dễ dàng hơn để tìm kiếm các thư mục con trong /usr.

Không may mắn, các thư mục con trong /usr không thể ghi.

Thư mục dễ dàng ghi có lẽ là /tmp. Ở điểm này vì /tmp không hiển thị trong PATH vì vậy chúng ta cần thêm nó. Lệnh export PATH=/tmp:$PATH có thể làm được điều đó.

Lúc này tập lệnh path cũng sẽ tìm kiếm trong thư mục /tmp 1 file thực thi tên là thm. Việc tạo lệnh này khá đơn giản bằng cách sao chép /bin/bash trong thm.

Chúng ta đã cấp quyền thực thi cho bản sao chép của /bin/bash, lưu ý là tại thời điểm này nó sẽ chạy với quyền của người dùng bình thường. Điều làm cho khả năng leo thang trong bối cảnh này là tập lệnh path sẽ chạy với đặc quyền root.

# **Leo thang đặc quyền : NFS**

Các phương hướng leo thang đặc quyền không bị giới hạn với truy cập nội bộ. Các thư mục shared và giao diện quản trị từ xa như SSH và telnet cũng có thể giúp bạn giành được quyền root trên hệ thống đích. Một vài trường hợp sẽ yêu cầu cả hai hướng tấn công, tìm 1 SSH private key của root trên hệ thống đích và kết nối qua SSH với đặc quyền root thay vì cố gắng gia tăng mức độ đặc quyền của người dùng.

Một phương hướng khác liên quan đến ctf và các bài kiểm tra là network shell bị cấu hình sai. Phương hướng này thường được nhìn thấy trong cam kết kiểm thử khi 1 bản sao lưu hệ thống mạng được hiển thị.

Cấu hình NFS (Netword File Sharing) được giữ trong /etc/exports. Tệp này được tạo trong quá trình cài đặt NFS và có thể được đọc bởi người dùng.

Thành phần quan trọng đối với phương hướng leo thang đặc quyền này là lựa chọn “no\_root\_squash” bạn có thể thấy ở trên. Mặc định, NFS sẽ thay đổi người dùng root thành nfsnobody và loại bỏ bất kỳ tệp nào hoạt động với quyền root. Nếu lựa chọn “no\_root\_squash” được hiển thị ở 1 bản share có thể ghi, chúng ta có thể tạo 1 tệp thực thi với SUID bit set và chạy nó trên hệ thống đích.

Chúng ta sẽ bắt đầu liệt kê các shares gắn kết từ máy tấn công.

Chúng ta sẽ mount một trong các shares có “no\_root\_squash” đến máy tấn công và bắt đầu xây dựng 1 tệp thực thi.

Vì chúng ta có thể đặt SUID bit, 1 tệp thực thi đơn giản sẽ chạy  /bin/bash trên hệ thống đích sẽ làm việc đó.

Khi biên dịch đoạn mã chúng ta sẽ đặt SUID bit.

Bạn sẽ thấy cả hai tệp (nfs.c và nfs được hiển thị trên hệ thống đích). Chúng ta đã làm việc trên share đã được gắn kết vì vậy không cần vận chuyển nó.

Lưu ý là tệp thực thi nfs có SUID bit set trên hệ thống đích và chạy với đặc quyền root.