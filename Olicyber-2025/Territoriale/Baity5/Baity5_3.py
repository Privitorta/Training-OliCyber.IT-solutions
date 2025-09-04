import base64

encoded_flag = 'Ao(mgHYtQJARB^:F^J`7F`(_sD)5Nj?X[eY1gaj2@:rqYDIYA2ARo.^DI5_=BlnVX?Y)&JAnEtX215'

try:
    decoded_flag = base64.a85decode(encoded_flag.encode()).decode('utf-8')
    print(f"flag: {decoded_flag}")
except Exception as e:
    print(f"errore nella decodifica: {e}")