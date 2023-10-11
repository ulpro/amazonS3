import boto3
import os

def upload_file_to_s3(file_path, bucket_name, object_name):
    # Créer une session AWS
    session = boto3.Session(
        aws_access_key_id='VOTRE_ACCESS_KEY',
        aws_secret_access_key='VOTRE_SECRET_ACCESS_KEY'
    )

    # Créer une instance du client S3
    s3_client = session.client('s3')

    # Charger le fichier dans le bucket S3
    try:
        with open(file_path, 'rb') as file:  # Ouvrir le fichier en mode binaire
            s3_client.put_object(Body=file, Bucket=bucket_name, Key=object_name)  # Utiliser object_name à la place de s3_key
    except Exception as e:
        print("Erreur lors du téléchargement du fichier sur S3:", str(e))

# Obtenir le chemin absolu du fichier à télécharger
file_path = os.path.abspath('chemin/vers/votre/fichier.txt')

# Spécifier le nom du bucket S3
bucket_name = 'nom-de-votre-bucket'

# Spécifier le nom du fichier sur S3
object_name = 'nom-du-fichier-sur-s3.txt'

# Appeler la fonction pour télécharger le fichier mis à jour sur S3
upload_file_to_s3(file_path, bucket_name, object_name)