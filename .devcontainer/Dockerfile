# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.205.2/containers/debian/.devcontainer/base.Dockerfile

# [Choice] Debian version (use bullseye or stretch on local arm64/Apple Silicon): bullseye, buster, stretch
ARG VARIANT="buster"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# https://stackoverflow.com/a/56748289
ARG VARIANT

# setup custom apt repository
RUN mkdir -p /usr/local/share/keyrings && gpg --list-keys \
    && gpg --no-default-keyring --keyring /usr/local/share/keyrings/skywrangler-archive-keyring.gpg \
    --keyserver keyserver.ubuntu.com --recv-keys B9B2C01AE12272D7 \
    && echo "deb [signed-by=/usr/local/share/keyrings/skywrangler-archive-keyring.gpg] http://archive.ablerobots.com/skywrangler $VARIANT main" > /etc/apt/sources.list.d/skywrangler.list

# install depedencies
RUN dpkg --add-architecture armhf && apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends python3-setuptools \
    python3-aiogrpc, python3-grpcio, python3-protobuf \
    devscripts debhelper dh-python git-buildpackage dput lintian bash-completion

COPY devscripts.conf /etc/
COPY dput.cf /etc/
COPY git-to-deb.sh /etc/profile.d/
