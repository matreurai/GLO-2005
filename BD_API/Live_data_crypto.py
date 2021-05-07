from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
import logging
import os
import time
import threading

#https://docs.python.org/3/library/logging.html#logging-levels
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

binance_websocket_api_manager = BinanceWebSocketApiManager()


def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is False:
            time.sleep(0.01)
        else:
            try:
                # remove # to activate the print function:
                print(oldest_stream_data_from_stream_buffer)
            except Exception:
                # not able to process the data? write it back to the stream_buffer
                binance_websocket_api_manager.add_to_stream_buffer(oldest_stream_data_from_stream_buffer)


# start a worker process to process to move the received stream_data from the stream_buffer to a print function
worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer, args=(binance_websocket_api_manager,))
worker_thread.start()

markets = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'EOSETH']
# print("\r\n========================================== Starting aggTrade ==========================================\r\n")
# # start
#
# aggtrade_stream_id = binance_websocket_api_manager.create_stream(["aggTrade"], markets)
# time.sleep(7)
# # stop
# binance_websocket_api_manager.stop_stream(aggtrade_stream_id)
# time.sleep(2)
# print("\r\n=========================================== Stopped aggTrade ==========================================\r\n")
# #
# print("\r\n====================================== Starting trade and kline_1m ====================================\r\n")
# trade_stream_id = binance_websocket_api_manager.create_stream(["trade"], markets)
# kline_1m_stream_id = binance_websocket_api_manager.create_stream("kline_1m", markets)
# time.sleep(7)
# binance_websocket_api_manager.stop_stream(trade_stream_id)
# binance_websocket_api_manager.stop_stream(kline_1m_stream_id)
# time.sleep(2)
# print("\r\n====================================== Stopped trade and kline_1m =====================================\r\n")

# print("\r\n======================================== Starting ticker ==============================================\r\n")
# ticker_bnbbtc_stream_id = binance_websocket_api_manager.create_stream(["ticker"], markets)
# time.sleep(7)
# binance_websocket_api_manager.stop_stream(ticker_bnbbtc_stream_id)
# time.sleep(2)
# print("\r\n======================================== Stopped ticker ===============================================\r\n")
#
# print("\r\n========================================== Starting miniticker ========================================\r\n")
# miniticker_stream_id = binance_websocket_api_manager.create_stream(["miniTicker"], markets)
# time.sleep(7)
# binance_websocket_api_manager.stop_stream(miniticker_stream_id)
# time.sleep(2)
# print("\r\n========================================= Stopped miniticker  =========================================\r\n")
#
# print("\r\n========================================== Starting kline_5m ==========================================\r\n")
# kline_5m_stream_id = binance_websocket_api_manager.create_stream(["kline_5m"], markets)
# time.sleep(7)
# binance_websocket_api_manager.stop_stream(kline_5m_stream_id)
# time.sleep(2)
# print("\r\n========================================= Stopped kline_5m  ===========================================\r\n")
#
# print("\r\n=========================================== Starting depth5 ===========================================\r\n")
# depth5_stream_id = binance_websocket_api_manager.create_stream(["depth5"], markets)
# time.sleep(7)
# binance_websocket_api_manager.stop_stream(depth5_stream_id)
# time.sleep(2)
# print("\r\n========================================== Stopped depth5  ============================================\r\n")
#
# print("\r\n========================================== Starting depth =============================================\r\n")
# depth_stream_id = binance_websocket_api_manager.create_stream(["depth"], markets)
# time.sleep(7)
# binance_websocket_api_manager.stop_stream(depth_stream_id)
# time.sleep(2)
# print("\r\n============================================ Stopped depth  ===========================================\r\n")
#
print("\r\n========================================== Starting !miniticker ========================================\r\n")
miniticker_stream_id = binance_websocket_api_manager.create_stream(["arr"], ["!miniTicker"])\

time.sleep(7)
binance_websocket_api_manager.stop_stream(miniticker_stream_id)
time.sleep(2)
# print("\r\n========================================= Stopped !miniticker  =========================================\r\n")
#
# print("\r\n========================================== Starting ticker all ========================================\r\n")
# ticker_all_stream_id = binance_websocket_api_manager.create_stream(["arr"], ["!ticker"])
# time.sleep(7)
# binance_websocket_api_manager.stop_stream(ticker_all_stream_id)
# time.sleep(2)
# print("\r\n=========================================== Stopped ticker all ========================================\r\n")
#
# print("\r\n=================================== Starting multi multi socket =======================================\r\n")
# channels = {'trade', 'kline_1', 'kline_5', 'kline_15', 'kline_30', 'kline_1h', 'kline_12h', 'kline_1w',
#             'miniTicker', 'depth20'}
# print(channels)
# print(markets, "\r\n")
# time.sleep(3)
# multi_multi_stream_id = binance_websocket_api_manager.create_stream(channels, markets)
# time.sleep(3)
# binance_websocket_api_manager.stop_stream(multi_multi_stream_id)
# time.sleep(2)
# print("\r\n================================== Stopped multi multi socket  ========================================\r\n")
#
# print("\r\n============================= Starting multi multi socket subscribe ===================================\r\n")
# channels = {'trade', 'kline_1', 'kline_5', 'kline_15', 'kline_30', 'kline_1h', 'kline_12h', 'kline_1w',
#             'miniTicker', 'depth20', '!miniTicker', '!ticker'}
# multi_multi_stream_id = binance_websocket_api_manager.create_stream(channels, markets)
# time.sleep(5)
# binance_websocket_api_manager.stop_stream(multi_multi_stream_id)
# time.sleep(2)
# print("\r\n============================== Stopped multi multi socket subscribe ===================================\r\n")


print("\r\n=============================== Stopping BinanceWebSocketManager ======================================\r\n")
binance_websocket_api_manager.stop_manager_with_all_streams()
print("finished!")
