# from PIL import Image
# from PIL import ImageFilter
from pydub import AudioSegment
import simpleaudio as sa

# #Manipulasi Gambar dengan Pillow
# # Memuat gambar
# image = Image.open('alam1.jpeg')

# # Menyimpan gambar
# image.save('result.jpg')

# cropped_image = image.crop((10, 10, 200, 200))
# cropped_image.save('cropped_result.jpg')

# resized_image = cropped_image.resize((100, 100))
# resized_image.save('resized_result.jpg')

# filtered_image = resized_image.filter(ImageFilter.BLUR)
# filtered_image.save('filtered_result.jpg')

# # Jika gambar dalam mode RGBA, ubah menjadi RGB
# if filtered_image.mode == 'RGBA':
#     filtered_image = filtered_image.convert('RGB')

##Memuat dan Menyimpan File Audio
# Memuat file audio
audio = AudioSegment.from_file('MattaroAda.mp3')

# Mengonversi ke WAV (opsional, jika formatnya bukan WAV)
audio.export('result.wav', format='wav')

# Memutar audio
wave_obj = sa.WaveObject.from_wave_file('result.wav')
play_obj = wave_obj.play()

# Pemotongan
clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')

# Penggabungan
combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

# Konversi Format
audio.export('result.wav', format='wav')

# Pengaturan Volume
louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')

# Menunggu sampai audio selesai diputar
play_obj.wait_done()

