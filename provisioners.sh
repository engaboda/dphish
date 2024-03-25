# update your existing list of packages:
apt update -y
# Next, install a few prerequisite packages which let apt use packages over HTTPS:
apt install apt-transport-https ca-certificates curl software-properties-common -y
#Then add the GPG key for the official Docker repository to your system:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Add the Docker repository to APT sources:
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" -y
# install Docker:
apt install docker-ce -y
# If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group:
usermod -aG docker ${USER}
# To apply the new group membership, log out of the server and back in, or type the following:
# You will be prompted to enter your user’s password to continue.
su - ${USER}

# to channel layer
docker run -d -p 6379:6379 redis

# for message broker
docker run -d -p 5672:5672 rabbitmq

# install requirements for django project
apt install python3-pip -y
pip install -r requirements