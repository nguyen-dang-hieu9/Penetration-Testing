# **Khái niệm:**

OSI (Open Systems Interconnection Model) là 1 mô hình cơ bản được dùng trong mạng.

Nó cung cấp 1 khuôn khổ về cách tất cả thiết bị mạng sẽ gửi, nhận và thông dịch dữ liệu.

Một lợi ích khác của mô hình OSI là các thiết bị có thể có những thiết kế và chức năng khác nhau trên mạng trong khi giao tiếp. Dữ liệu gửi qua mạng theo mô hình này có thể được hiểu bởi những thiết bị khác. 

Nó có 7 lớp, mỗi lớp có trách nhiệm khác nhau và xếp từ lớp 1 đến lớp 7.

Ở mỗi lớp dữ liệu đi qua, những quá trình cụ thể sẽ xảy ra và một ít thông tin được thêm vào dữ liệu này.

 <img width="468" height="300" alt="image" src="https://github.com/user-attachments/assets/adf664da-1053-471a-b7f1-829fa04352b8" />

# **Lớp 7: Ứng dụng**

Lớp ứng dụng của mô hình OSI là lớp bạn quen thuộc nhất. Vì lớp ứng dụng là lớp trong đó có các giao thức và qui tắc để xác định cách người dùng nên tương tác với dữ liệu được gửi hoặc nhận.

Các ứng dụng hàng ngày như email, trình duyệt hay phần mềm duyệt tập tin trên máy chủ như FileZilla cung cấp 1 giao diện thân thiện để người dùng tương tác với dữ liệu được nhận hoặc gửi đi. Những giao thức khác bao gồm DNS là cách địa chỉ trang web được dịch sang địa chỉ IP. 

 <img width="468" height="238" alt="image" src="https://github.com/user-attachments/assets/474d2d9c-6f94-41b3-a93f-ee4e9c35caf1" />

# **Lớp 6: Trình bày**

Lớp 6 của mô hình OSI là lớp mà sự tiêu chuẩn bắt đầu xảy ra. Vì những nhà phát triển phần mềm có thể phát triển bất cứ phần mềm nào như email , dữ liệu vẫn được xử lí theo cách cũ- không có vấn đề gì về cách phần mềm hoạt động.

Lớp này dịch dữ liệu đến và từ lớp ứng dụng. Máy tính nhận cũng sẽ hiểu dữ liệu được gửi đến máy tính ở 1 định dạng khác. Ví dụ, khi bạn gửi 1 email, người dùng khác có thể có email khác với bạn nhưng nội dung vẫn giống nhau.

Tính bảo mật như mã hóa dữ liệu (HTTPs) cũng xảy ra ở lớp này.

# **Lớp 5: Phiên** 

Khi dữ liệu đã được dịch đúng từ lớp 6, lớp phiên sẽ bắt đầu tạo 1 kết nối đến máy tính khác để dữ liệu đưa đến. Khi kết nối được thiết lập, 1 phiên sẽ được tạo ra.

Lớp phiên đồng bộ hóa hai máy tính để đảm bảo rằng chúng ở cùng 1 trang trước khi dữ liệu được gửi và nhận.

Sau đó, lớp phiên sẽ bắt đầu chia dữ liệu thành những gói nhỏ, bắt đầu gửi. Việc chia này rất có lợi vì nếu kết nối mất đi, những gói vẫn chưa được gửi sẽ gửi lại

Cái đáng chú ý nhất là những phiên là duy nhất. Điều này có nghĩa là dữ liệu không thể đi qua những phiên khác mà thực tế chỉ đi qua từng phiên.

# **Lớp 4: Vận chuyển**

Lớp 4 của mô hình OSI đóng vai trò thiết yếu trong việc truyền dữ liệu qua mạng và có thể khó nắm bắt. Khi dữ liệu được gửi giữa các thiết bị, nó theo 1 trong 2 giao thức sau: 

* TCP
    
* UDP
    

TCP (Transmission Control Protocol) là giao thức giúp duy trì sự kết nối giữa hai thiết bị trong khoảng thời gian cần thiết để gửi và nhận dữ liệu.

Không chỉ vậy, TCP còn kết hợp kiểm tra lỗi. Kiểm tra lỗi là cách TCP có thể đảm bảo dữ liệu được gửi từ những gói nhỏ trong lớp phiên sau đó được nhận và tập hợp lại theo đúng thứ tự.

Cùng tổng hợp lại những ưu điểm và khuyết điểm của TCP:

| **Ưu điểm** | **Khuyết điểm** |
| --- | --- |
| Đảm bảo độ chính xác của dữ liệu | Yêu cầu 1 kết nối rõ ràng giữa hai thiết bị. Nếu 1 mẫu dữ liệu nhỏ không được nhận thì toàn bộ dữ liệu không thể dùng được |
| Có khả năng đồng bộ 2 thiết bị tránh tràn ngập dữ liệu của nhau | Kết nối chậm có thể làm tắc nghẽn thiết bị khác vì kết nối sẽ chỉ duy trì cho máy nhận trong toàn bộ thời gian |
| Thực hiện nhiều qui trình đáng tin cậy | TCP rõ ràng chậm hơn UDP vì nhiều công việc phải làm hơn bởi những thiết bị dùng giao thức này. |

TCP được dùng cho những tình huống như chia sẻ tập tin, duyệt web hay gửi thư. Vì những dịch vụ đó yêu cầu dữ liệu phải chính xác và đầy đủ.

Chúng ta có thể thấy 1 hình ảnh của con chó được chia ra thành những gói dữ liệu nhỏ từ máy chủ web, trong đó máy tính sẽ sắp xếp lại hình ảnh cho đúng trình tự.

 <img width="468" height="175" alt="image" src="https://github.com/user-attachments/assets/e37f6e1d-760a-4a43-8908-9310347ae56d" />

Bây giờ cùng tìm hiểu UDP (User Datagram Protocol). Giao thức này gần như không tiên tiến như người anh em của nó – TCP.

Nó không đem lại nhiều tính năng như TCP như kiểm tra lỗi và sự đáng tin cậy. Trong thực tế, bất cứ dữ liệu nào được gửi qua UDP đều được gửi đến máy tính  cho dù nó có đến đó hay không. Không có sự đồng bộ hóa giữa hai thiết bị hoặc bảo đảm.

| **Ưu điểm** | **Khuyết điểm** |
| --- | --- |
| UDP nhanh hơn rất nhiều TCP | UDP không quan tâm dữ liệu có nhận được không |
| UDP để cho lớp ứng dụng kiểm soát tốc độ những gói tin được gửi | Nó khá linh hoạt cho nhà phát triển phần mềm. |
| UDP không duy trì kết nối trên 1 thiết bị mà TCP làm | Các kết nối không ổn định dẫn đến trải nghiệm tồi tệ cho người dùng |

Chúng ta có thể thấy chỉ gói 1 và gói 3 được nhận bởi máy tính. Điều này có nghĩa là 1 nửa bức tranh bị bỏ.

 <img width="468" height="175" alt="image" src="https://github.com/user-attachments/assets/e768b66f-ab40-4044-a3be-ce8480118f97" />

UDP rất hữu dụng trong tình huống có 1 lượng nhỏ dữ liệu được gửi. Ví dụ, giao thức được dùng để khám phá những thiết bị (ARP và DHCP)  hoặc những tập tin lớn như video (vẫn OK nếu một vài phần của video bị pixel. Pixel là những dữ liệu bị mất đi)

# **Lớp 3: Mạng**

Lớp thứ 3 của mô hình OSI là nơi mà định tuyến và tổng hợp lại dữ liệu xảy ra (từ những gói tin nhỏ đến gói tin lớn hơn).

Đầu tiên, định tuyến xác định con đường tối ưu nhất mà những gói dữ liệu nên được gửi.

Trong khi một vài giao thức ở lớp này xác định đường dẫn tối ưu mà dữ liệu sẽ đi đến 1 thiết bị, chúng ta chỉ nên biết về sự tồn tại của giai đoạn này trong lớp mạng.

Những giao thức đó bao gồm OSPF và RIP. Những yếu tố quyết định tuyến đường tối ưu nhất:

Tuyến đường nào là ngắn nhất? Nói cách khác có ít nhất bao nhiêu thiết bị mà gói tin cần truyền đến

Tuyến đường nào đáng tin cậy nhất? Đã có bao nhiêu gói tin bị mất trên tuyến đường này??

Tuyến đường nào có kết nối vật lý nhanh hơn? Có đường dẫn sử dụng kết nối bằng đồng hoặc bạc??

Ở lớp này, mọi thứ đều xử lí qua những địa chỉ IP như 192.168.1.100

Các thiết bị như routers có khả năng vận chuyển những gói tin bằng cách sử dụng địa chỉ IP của các thiết bị lớp 3.

# **Lớp hai: Đường dẫn dữ liệu** 

Lớp này tập trung vào địa chỉ vật lý của đường truyền. Nó nhận 1 gói tin từ lớp mạng (chứa địa chỉ IP của máy tính từ xa) và thêm địa chỉ MAC ở những điểm nhận. Trong mỗi máy tính kết nối mạng là thẻ giao diện mạng đi kèm với 1 địa chỉ MAC duy nhất để nhận dạng nó.

Khi thông tin được gửi qua mạng, địa chỉ vật lý được dùng để xác định nơi gửi thông tin.

Ngoài ra, lớp này còn hiển thị dữ liệu ở định dạng phù hợp cho việc truyền tải

# **Lớp 1: Vật Lý** 

Lớp này là 1 trong những lớp dễ hiểu biết nhất.

Nó nhắc đến những thành phần của phần cứng dùng trong mạng và là lớp thấp nhất

Những thiết bị dùng tín hiệu điện để truyền dữ liệu với nhau trong hệ thống nhị phân (0 và 1) 

Ví dụ, cáp quang kết nối các thiết bị.

 <img width="468" height="351" alt="image" src="https://github.com/user-attachments/assets/fa127a37-8e71-47cb-a57f-de82ce56c400" />
