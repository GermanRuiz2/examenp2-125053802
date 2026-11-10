FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    openjdk-17-jdk python3 wget ssh openssh-server tar \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# Comandos para la extraccion de Hadoop:
RUN wget -q https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz -C /opt/ && \
    mv /opt/hadoop-${HADOOP_VERSION} /opt/hadoop && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

RUN echo "export JAVA_HOME=${JAVA_HOME}" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh

# Verificación exigida por la rúbrica (Inciso A1)
RUN hadoop version

# Configuración de SSH sin contraseña
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys

CMD service ssh start && tail -f /dev/null