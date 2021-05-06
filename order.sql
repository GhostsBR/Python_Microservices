-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06-Maio-2021 às 21:01
-- Versão do servidor: 10.4.17-MariaDB
-- versão do PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `proway`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `order`
--

CREATE TABLE `order` (
  `id` varchar(255) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `item_description` text NOT NULL,
  `item_quantity` int(11) NOT NULL,
  `item_price` float NOT NULL,
  `total_value` float NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `order`
--

INSERT INTO `order` (`id`, `user_id`, `item_description`, `item_quantity`, `item_price`, `total_value`, `created_at`, `updated_at`) VALUES
('293159c3dd0d457dbde3628bd88686ff', '22bbba6dfadb48c7932b9c3a5fa71bae', 'teste', 2, 10, 20, '2021-05-06 13:01:58', '2021-05-06 13:01:58'),
('6c73d885c3874f82ae68932466e646a9', '22bbba6dfadb48c7932b9c3a5fa71bae', 'teste', 2, 10, 20, '2021-05-06 13:25:47', '2021-05-06 13:25:47'),
('8ffd6cdae061419bb191521fcfb71d67', '22bbba6dfadb48c7932b9c3a5fa71bae', 'teste', 2, 10, 20, '2021-05-06 13:25:20', '2021-05-06 13:25:20');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_FK` (`user_id`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_FK` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
