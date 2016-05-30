CREATE TABLE `TDays` (
  `TradingCalendar` varchar(10) NOT NULL DEFAULT 'SSE' COMMENT '交易所',
  `DateTime` date NOT NULL DEFAULT '1983-01-05' COMMENT '交易日',
  PRIMARY KEY (`TradingCalendar`,`DateTime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='交易日表';

CREATE TABLE `WSETSecurityCode` (
  `begin_date` date NOT NULL DEFAULT '1983-01-05' COMMENT '交易日开始',
  `end_date` date NOT NULL DEFAULT '1983-01-05' COMMENT '交易日结束',
  `wind_code` varchar(32) NOT NULL DEFAULT '' COMMENT 'Wind代码',
  `sec_name` varchar(32) NOT NULL DEFAULT '' COMMENT '证券名称',
  PRIMARY KEY (`begin_date`,`wind_code`,`sec_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='证券代码表';

CREATE TABLE `WSI` (
  `TradeTime` datetime NOT NULL DEFAULT '1983-01-05 09:31:00' COMMENT '交易时间',
  `SecurityCode` varchar(20) NOT NULL DEFAULT '' COMMENT '证券代码',
  `open` decimal(12,3) DEFAULT '0.000' COMMENT '开盘价',
  `high` decimal(12,3) DEFAULT '0.000' COMMENT '最高价',
  `low` decimal(12,3) DEFAULT '0.000' COMMENT '最低价',
  `close` decimal(12,3) DEFAULT '0.000' COMMENT '收盘价',
  `volume` decimal(15,2) DEFAULT '0.00' COMMENT '成交量',
  `amt` decimal(18,3) DEFAULT '0.000' COMMENT '成交额',
  `chg` decimal(12,3) DEFAULT '0.000' COMMENT '涨跌',
  `pct_chg` decimal(10,5) DEFAULT '0.00000' COMMENT '涨跌幅',
  `oi` decimal(15,2) DEFAULT '0.00' COMMENT '持仓量',
  `BIAS_5` decimal(16,8) DEFAULT '0.00000000' COMMENT '乖离率_5',
  `BIAS_12` decimal(16,8) DEFAULT '0.00000000' COMMENT '乖离率_12',
  `BOLL_5_2_MID` decimal(16,8) DEFAULT '0.00000000' COMMENT '布林带-5_2_MID',
  `BOLL_20_2_MID` decimal(16,8) DEFAULT '0.00000000' COMMENT '布林带-20_2_MID',
  `DMI_14_6_PDI` decimal(16,8) DEFAULT '0.00000000' COMMENT '趋向标准-14_6_PDI_中长期',
  `EXPMA_5` decimal(16,8) DEFAULT '0.00000000' COMMENT '指数平滑移动评价-5',
  `EXPMA_12` decimal(16,8) DEFAULT '0.00000000' COMMENT '指数平滑移动评价-12',
  `KDJ_9_3_3_K` decimal(16,8) DEFAULT '0.00000000' COMMENT '随机指标_9_3_3_K_中短期',
  `MA_5` decimal(16,8) DEFAULT '0.00000000' COMMENT '简单移动平均_5',
  `MACD_26_12_9_DIFF` decimal(16,8) DEFAULT '0.00000000' COMMENT '指数平滑异同平均_26_12_9_DIFF',
  `RSI_6` decimal(16,8) DEFAULT '0.00000000' COMMENT '相对强弱指标_6_短期',
  PRIMARY KEY (`TradeTime`,`SecurityCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='日内分钟数据';
