-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th9 18, 2024 lúc 06:17 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `test`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `user_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `full_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `isadmin` int(10) UNSIGNED DEFAULT NULL,
  `telephone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `profile_picture` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `user`
--

INSERT INTO `user` (`id`, `user_name`, `password`, `full_name`, `isadmin`, `telephone`, `address`, `profile_picture`, `email`) VALUES
(1, 'admin', 'admin1', 'hungdaica', 1, NULL, NULL, NULL, NULL),
(2, 'hung', 'hung', '', 0, NULL, NULL, NULL, NULL),
(4, 'binh', 'newpassword123', '', 0, NULL, NULL, NULL, NULL),
(5, 'binh1', '1234', '', 0, NULL, NULL, NULL, NULL),
(7, 'hungdaica', '$2y$10$uswuDXDnAAdK.DcTfdGid.Mtw69R7ErVHoQPpWIvo0yL8FSQYcLJa', 'hungdaica', 0, NULL, NULL, NULL, NULL),
(8, 'hung1', 'hung1', 'HungPK', 1, '0978825499', 'Hà Nội', 'uploads/8_11.jpg', 'hungnp@gmail.com'),
(10, 'test', 'test', 'test', 1, '0978825499', 'Hà Nội', 'uploads/8_11.jpg', 'hunglnp@gmail.com'),
(11, 'user', 'user', 'user', 0, '0978825499', 'Ha Noi', 'uploads/11_lovekey.jpg', 'hungnp@gmail.com'),
(12, 'hungpk', '$2y$10$o7uWX64iYrDi4tvJgR.rK.y4nxkYGCfsb59lsLPe0HIroXJSdt1vm', 'hung', 0, NULL, NULL, NULL, NULL),
(228, 'hungdc', 'hungdc', NULL, 1, NULL, NULL, NULL, NULL);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=229;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
