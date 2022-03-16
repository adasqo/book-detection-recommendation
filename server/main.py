import multiprocessing as mp
mp.set_start_method('fork')

from src.api.main import start_api

if __name__ == '__main__':
   start_api()
   