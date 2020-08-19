terraform init /tmp/terraformLab/
terraform plan -env 'accessKey=$accessKey1' -env 'secretKey=$accessSecret1' /tmp/terraformLab/
terraform apply -auto-approve /tmp/terraformLab
