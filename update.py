import boto3
import os

def upload_file_to_s3(file_path, bucket_name, object_name):
    # Créer une session AWS
    session = boto3.Session(
        aws_access_key_id='AKIA3PHTF3PC4TPQLUFG;',
        aws_secret_access_key='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;l'
    )

    # Créer une instance du client S3
    s3_client = session.client('s3')

    # Charger le fichier dans le bucket S3
    try:
        with open(file_path, 'rb') as file:  # Ouvrir le fichier en mode binaire
            s3_client.put_object(Body=file, Bucket=bucket_name, Key=object_name)  # Utiliser object_name à la place de s3_key
            print("mise a jour  reussit")
    except Exception as e:
        print("Erreur lors du téléchargement du fichier sur S3:", str(e))

# Obtenir le chemin absolu du fichier à télécharger
file_path = os.path.abspath('D:/projets/fichier.txt')

# Spécifier le nom du bucket S3
bucket_name = 'awss3-bucket1'

# Spécifier le nom du fichier sur S3
object_name = 'test.txt'

# Appeler la fonction pour télécharger le fichier mis à jour sur S3
upload_file_to_s3(file_path, bucket_name, object_name)