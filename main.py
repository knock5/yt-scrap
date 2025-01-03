from googleapiclient.discovery import build
import pandas as pd

# Masukkan API Key Anda
api_key = 'API_KEY'

# ID video yang ingin diambil komentarnya
video_id = 'VIDEO_ID'

# Membuat client YouTube API
youtube = build('youtube', 'v3', developerKey=api_key)

# Fungsi untuk mengambil komentar dari video
def get_all_video_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100
    )

    while request:
        response = request.execute()
        for item in response['items']:
            # Mengambil komentar dan nama penulis
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            published_at = item['snippet']['topLevelComment']['snippet']['publishedAt']
            
            comments.append({
                'Author': author,
                'Comment': comment,
                'Published At': published_at
            })

        # Mendapatkan token untuk halaman berikutnya, jika ada
        request = youtube.commentThreads().list_next(request, response)

    return comments

# Mendapatkan semua komentar
try:
    print("Mengambil komentar dari video...")
    all_comments = get_all_video_comments(video_id)

    # Menyimpan data ke dalam file CSV
    output_file = 'youtube_comments.csv'
    df = pd.DataFrame(all_comments)
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Data komentar berhasil disimpan ke file: {output_file}")

    # Membaca dan menampilkan data menggunakan pandas
    df_read = pd.read_csv(output_file)
    print("\nData Komentar yang Diambil:")
    print(df_read.head())  # Menampilkan 5 data pertama
except Exception as e:
    print(f"Terjadi error: {e}")
