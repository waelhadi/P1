import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_data(encrypted_data, key, iv):
    """
    فك تشفير البيانات باستخدام AES.
    
    :param encrypted_data: النص المشفر
    :param key: المفتاح السري
    :param iv: متجه التهيئة (IV)
    :return: البيانات المفككة
    """
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), AES.block_size)
        return decrypted
    except Exception as e:
        print("Error during decryption:", e)
        return None

# مثال على الاستخدام
if __name__ == "__main__":
    encrypted_sample = "ضع هنا بيانات مشفرة للاختبار"
    key = b'secret_key_16byt'  # نفس المفتاح المستخدم في التشفير
    iv = b'iv_16_bytes_long'   # نفس متجه التهيئة

    decrypted_data = decrypt_data(encrypted_sample, key, iv)
    if decrypted_data:
        print("Decrypted data:", decrypted_data.decode())
