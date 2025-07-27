# **Giới thiệu về kết cấu mạng LAN**

Trải qua rất nhiều năm thí nghiệm và thực thi những thiết kế mạng khác nhau. Liên quan đến mạng, khi chúng ta nhắc đến thuật ngữ “topology”, chúng ta đang đề cập đến thiết kế hay giao diện mạng.

## **Kết cấu mạng dạng sao:**

Ý tưởng chính của mạng dạng sao là những thiết bị được kết nối qua 1 thiết bị mạng trung tâm như switch hay hub. Kết cấu này được tìm thấy khá phổ biến vì độ tin cậy và khả năng mở rộng của nó mặc cho chi phí.

Bất cứ thông tin gì được gửi đến 1 thiết bị trong kết cấu này phải được thông qua thiết bị trung tâm mà nó kết nối. 

Bởi vì nhiều cáp hơn và việc mua thiết bị mạng chuyên dụng rất cần thiết cho kết cấu này, nó thường mắc hơn những kết cấu khác. Tuy vậy, nó vẫn cung cấp rất nhiều lợi ích. Ví dụ, kết cấu này có khả năng mở rộng hơn, điều đó có nghĩa là rất dễ dàng dể thêm nhiều thiết bị hơn khi nhu cầu về mạng tăng lên.

Không may mắn, quy mô của mạng càng lớn, càng cần bảo trì mạng nhiều hơn. Sự phụ thuộc vào bảo trì ngày càng tăng cũng có thể làm cho việc khắc phục sự cố trở nên khó khăn hơn. Hơn nữa , kết cấu dạng sao này rất dễ bị thất bại. Ví dụ, nếu phần cứng trung tâm kết nối các thiết bị thất bại, những thiết bị khác không thể nhận hay gửi dữ liệu. Rất may, các thiết bị phần cứng trung tâm này thường rất mạnh mẽ. 

 <img width="468" height="283" alt="image" src="https://github.com/user-attachments/assets/f95807d2-fdb9-4424-8bec-a00e9741ea8a" />

## **Kết cấu mạng dạng Bus:**

Loại kết nối này dựa trên 1 kết nối duy nhất được gọi là cáp xương sống.

Loại kết nối này tương tự như chiếc lá trên cây theo nghĩa là những thiết bị xuất phát từ các nhánh của cáp này.

Vì tất cả dữ liệu dành cho mỗi thiết bị đều đi qua 1 cáp duy nhất. Nó dễ trở nên chậm và bị tắc nghẽn nếu những thiết bị đồng thời yêu cầu dữ liệu. Sự tắc nghẽn này rất khó khắc phục vì rất khó xác định thiết bị nào đang gặp vấn đề.

Tuy vậy , kết cấu này là 1 trong những cấu trúc liên kết dễ dàng hơn và tiết kiệm chi phí để thiết lập.

Cuối cùng, 1 điểm bất lợi khác của kết cấu này là có rất ít sự dư thừa nếu xảy ra lỗi. Nếu cáp bị phá vỡ, những thiết bị sẽ không còn nhận hay gửi dữ liệu theo tuyến được. 

 <img width="468" height="241" alt="image" src="https://github.com/user-attachments/assets/8d250b0b-a853-46e1-b9c2-59960328302c" />

## **Kết cấu mạng dạng Ring:**

Những thiết bị như máy tính được kết nối trực tiếp với máy khác tạo thành 1 vòng lặp. Điều này có nghĩa là cần rất ít cáp và sự phụ thuộc vào phần cứng chuyên dụng như trong kết cấu dạng sao.

Kết cấu dạng ring làm việc bằng cách gửi dữ liệu qua vòng lặp cho đến khi nó đến thiết bị mong muốn,  bằng việc sử dung thiết bị khác để truyền dữ liệu. Điều thú vị là, 1 thiết bị sẽ chỉ gửi dữ liệu được nhận từ thiết bị khác nếu nó không có gì để gửi. Nếu thiết bị có dữ liệu để gửi, nó sẽ gửi dữ liệu của chính nó trước khi gửi dữ liệu từ thiết bị khác.

Vì dữ liệu chỉ có 1 hướng để truyền, nó rất dễ khắc phục khi có lỗi xảy ra. Tuy nhiên nó là 1 con dao hai lưỡi vì nó không phải là cách hiệu quả để truyền dữ liệu qua mạng vì nó có thể phải đi qua nhiều thiết bị khác trước khi đến máy tính nó mong muốn.

Cuối cùng, kết cấu mạng dạng ring rất ít bị tắc nghẽn vì không có lưu lượng lớn mạng trong 1 lần. Tuy nhiên, chỉ cần cáp bị đứt hay thiết bị bị hỏng sẽ dẫn đến toàn bộ mạng bị hỏng.

 <img width="468" height="279" alt="image" src="https://github.com/user-attachments/assets/530bddc6-b04b-414e-870c-96836d1152ee" />

# **Switch**

Switches là những thiết bị chuyên dụng trong 1 mạng được thiết kế để tổng hợp nhiều thiết bị khác nhau như: máy tính, máy in hoặc bất kỳ thiết bị nào có khả năng kết nối mạng sử dụng ethernet. Các thiết bị khác nhau này cắm vào cổng của Switch.

Switches thường được tìm thấy ở những mạng lớn hơn như doanh nghiệp, trường học hoặc những mạng có kích thước tương tự, có nhiều thiết bị kết nối mạng.  Switches có thể kết nối 1 lượng lớn thiết bị bằng việc có các cổng 4, 8, 16, 24, 32 và 64 để các thiết bị cắm vào.

Switches có thể hoạt động ở lớp 2 và lớp 3 của mô hình OSI 

Lấy ví dụ switch ở lớp 2. Nó sẽ chuyển tiếp frames (nhớ là sẽ không có packets vì không có địa chỉ IP) cho những thiết bị kết nối bằng việc sử dụng địa chỉ MAC.

 <img width="468" height="419" alt="image" src="https://github.com/user-attachments/assets/7a014c76-bbe5-41a0-9e71-55dd643bb22d" />

Những switch này chịu trách nhiệm gửi frame cho đúng thiết bị.

Bây giờ hãy chuyển sang switch ở lớp 3. Nó phức tạp hơn lớp 2 vì chúng thực hiện một số trách nhiệm của bộ định tuyến. Chúng sẽ gửi frames đến đúng thiết bị (như lớp 2 làm) và packets đến những thiết bị sử dụng địa chỉ IP.

Cùng xem hình minh họa về cách switch lớp 3 hoạt động. Chúng ta thấy có 2 địa chỉ IP (đây là địa chỉ của mạng con)

* 192.168.1.1
    
* 192.168.2.1
    

Một công nghệ gọi là VLAN (Virtual Local Area Network) cho phép những thiết bị cụ thể trong 1 mạng được chia nhỏ. Điều này có nghĩa là chúng đều hưởng lợi từ những thứ như kết nối Internet. Sự tách biệt này đem lại biện pháp bảo mật vì chúng xác định cách các thiết bị giao tiếp với nhau.

 <img width="468" height="424" alt="image" src="https://github.com/user-attachments/assets/24f8e830-5bba-4580-b2ee-b20bf5027d6a" />

Trong bối cảnh trên, “Sales Department” và “Accounting Department” sẽ có thể truy cập Internet nhưng không thể giao tiếp với nhau (mặc dù chúng kết nối cùng switch)

Switches thường hiệu quả hơn đối thủ của chúng (hubs/repeaters). Switches theo dõi thiết bị nào được kết nối với cổng nào. Nhờ đó, khi chúng nhận 1 gói tin, thay vì lặp lại gói đó ở mỗi cổng mà hub đã làm, nó chỉ gửi đến 1 đối tượng nhất định. Nhờ đó giảm được lưu lượng mạng.

 <img width="468" height="245" alt="image" src="https://github.com/user-attachments/assets/7da08e08-72d6-40ee-9e93-e17ef42e3eba" />

Cả switches và routers đều có thể được kết nối với nhau. Điều này giúp tăng sự dư thừa của mạng bằng việc thêm nhiều đường dẫn dữ liệu. Nếu đường dẫn này bị hỏng, cái khác có thể được dùng. Mặc dù điều này có thể làm giảm toàn bộ hiệu suất của mạng vì những gói tin cần vận chuyển lâu hơn, nhưng không có thời gian chết.

# **Router:**

Công việc của router là kết nối các mạng và gửi dữ liệu giữa chúng. Nó làm việc này bằng định tuyến.

Định tuyến (routing) liên quan đến việc tạo 1 đường dẫn giữa các mạng để mà dữ liệu được vận chuyển thành công.

Định tuyến rất hữu dụng khi các thiết bị được kết nối bằng nhiều đường dẫn khác nhau, như ví dụ bên dưới:

 <img width="468" height="158" alt="image" src="https://github.com/user-attachments/assets/5ed2f91b-fe2c-4b38-b259-3dba7f9b4e11" />

Routers hoạt động ở lớp 3 trong mô hình OSI. 

Chúng thường có 1 giao diện tương tác (như trang web hay console) cho phép nhà quản trị cấu hình nhiều qui tắc như cổng chuyển tiếp hay tường lửa. 

Chúng ta có thể thấy mạng của máy tính A kết nối với mạng máy tính B bằng hai router ở giữa. Câu hỏi là nó sẽ đi đường nào? Những giao thức khác nhau sẽ quyết định đường dẫn nào sẽ được thực hiện. Các yếu tố quyết định bao gồm:

Đường ngắn nhất, đáng tin cậy nhất và có chất liệu nhanh hơn (đồng hay bạc)

# **Sơ lược về mạng con:**

Mạng có thể được tìm thấy ở nhiều hình dạng và kích thước – phạm vi từ nhỏ đến lớn.

Mạng con là thuật ngữ để chia mạng ra nhỏ hơn, mạng con trong chính nó.

Lấy doanh nghiệp làm ví dụ. Bạn sẽ có những phòng ban khác nhau như:

* Kế toán
    
* Tài chính
    
* Tài nguyên con người
    
 <img width="468" height="300" alt="image" src="https://github.com/user-attachments/assets/0b920822-8549-4899-8f1c-015fb9ecbfea" />

Trong khi bạn biết gửi thông tin đến đúng phòng ban trong thực tế thì mạng cũng cần biết. Nhà quản trị mạng dùng mạng con để phân loại và gán các phần cụ thể của mạng cho chúng.

Mạng con được tạo ra bằng cách chia nhỏ số lượng máy chủ có thể phù hợp với mạng, đại diện bởi 1 con số là subnet mask

 <img width="468" height="234" alt="image" src="https://github.com/user-attachments/assets/30540184-1e8a-4262-bbea-91a43f08ed02" />

1 subnet mask rất giống với địa chỉ IP

Mạng con dùng địa chỉ IP theo 3 cách khác nhau:

* Xác định địa chỉ mạng
    
* Xác định địa chỉ máy chủ
    
* Xác định cổng vào mặc định
    

| **Type** | **Purpose** | **Explanation** | **Example** |
| --- | --- | --- | --- |
| Network Address | This address identifies the start of the actual network and is used to identify a network's existence. | For example, a device with the IP address of 192.168.1.100 will be on the network identified by 192.168.1.0 | 192.168.1.0 |
| Host Address | An IP address here is used to identify a device on the subnet | For example, a device will have the network address of 192.168.1.1 | 192.168.1.100 |
| Default Gateway | The default gateway address is a special address assigned to a device on the network that is capable of sending information to another network | Any data that needs to go to a device that isn't on the same network (i.e. isn't on 192.168.1.0) will be sent to this device. These devices can use any host address but usually use either the first or last host address in a network (.1 or .254) | 192.168.1.254 |

Bây giờ trong những mạng nhỏ như ở nhà, sẽ không có cơ hội dùng mạng con vì không có đủ 254 thiết bị kết nối cùng một lúc.

Tuy nhiên những nơi như doanh nghiệp hay trụ sở sẽ có rất nhiều thiết bị (PCs, máy in, máy chụp hình và bộ cảm biến) thì mạng con sẽ xảy ra.

Việc phân chia mạng đem lại nhiều lợi ích như:

* Hiệu suất
    
* Bảo mật
    
* Toàn quyền kiểm soát
    

Ví dụ: Cùng đến 1 quán café trên đường. Quán café sẽ có hai mạng:

1. Một cho nhân viên, máy tính tiền, và những thiết bị khác
    
2. Một cho công chúng sử dụng
    

Mạng con cho phép bạn tách biệt hai trường hợp sử dụng mạng khác nhau trong khi vẫn có lợi ích được kết nối với các mạng lớn hơn như Internet

# **Giao thức ARP** 

Những thiết bị có thể xác định bằng hai cách: địa chỉ MAC và địa chỉ IP 

Giao thức ARP (Address Resolution Protocol) là công nghệ chịu trách nhiệm cho phép các thiết bị xác định trên mạng.

Đơn giản hơn, giao thức ARP cho phép 1 thiết bị liên kết địa chỉ MAC của nó với địa chỉ IP trên mạng. Mỗi thiết bị trên mạng sẽ ghi lại địa chỉ MAC gắn với thiết bị khác.

Khi những thiết bị muốn giao tiếp với nhau, chúng sẽ gửi 1 đoạn tin đến toàn bộ mạng để tìm kiếm thiết bị mong muốn. Những thiết bị có thể sử dụng giao thức ARP để tìm kiếm địa chỉ MAC của 1 thiết bị để giao tiếp

## **ARP hoạt động như thế nào?**

Mỗi thiết bị trên mạng có 1 nơi để lưu trữ thông tin gọi là bộ nhớ đệm. Trong bối cảnh của giao thức ARP, bộ nhớ đệm lưu trữ mã định danh của những thiết bị khác trên mạng.

Để ánh xạ hai mã định danh với nhau (địa chỉ IP và địa chỉ MAC), giao thức ARP gửi hai loại tin nhắn:

* ARP yêu cầu
    
* ARP phản hồi
    

Khi 1 ARP yêu cầu được gửi đi, 1 tin nhắc được truyền đến mọi thiết bị tìm thấy trên mạng, hỏi xem địa chỉ MAC của thiết bị có phù hợp với địa chỉ IP yêu cầu không. Nếu thiết bị có địa chỉ IP yêu cầu, ARP phản hồi sẽ trả về thiết bị ban đầu để xác nhận điều này. Thiết bị ban đầu sẽ nhớ nó và lưu trữ trong bộ nhớ đếm (đầu vào ARP).

Quá trình này được mô phỏng như sau:

 <img width="468" height="383" alt="image" src="https://github.com/user-attachments/assets/0fec4c78-ed1c-4951-a30f-08f00ee85153" />

# **Giao thức DHCP:** 

Địa chỉ IP có thể được gán thủ công bằng cách nhập chúng vào thiết bị hoặc tự động và phổ biến nhất là sử dụng máy chủ DHCP (Dynamic Host Configuration Protocol).

Khi 1 thiết bị kết nối mạng, nếu nó không được gán địa chỉ IP thủ công, nó sẽ gửi 1 yêu cầu (DHCP Discover) để xem có bất cứ máy chủ DHCP nào trên mạng không. Máy chủ DHCP sau đó sẽ phản hồi lại bằng địa chỉ IP mà thiết bị có thể sử dụng (DHCP Offer).

Sau đó, thiết bị sẽ  gửi 1 phản hồi xác nhận nó muốn địa chỉ IP đó (DHCP Request). Cuối cùng, máy chủ DHCP xác nhận quá trình này đã hoàn tất và thiết bị có thể sử dụng địa chỉ IP đó (DHCP ACK).

 <img width="468" height="539" alt="image" src="https://github.com/user-attachments/assets/747ad20b-d9a4-43e8-b59e-22f50695fa78" />
