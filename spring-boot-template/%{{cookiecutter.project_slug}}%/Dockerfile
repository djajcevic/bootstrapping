FROM eclipse-temurin:22.0.2_9-jdk
COPY target/app.jar ./app.jar
ADD https://github.com/grafana/grafana-opentelemetry-java/releases/download/v2.6.0-beta.2/grafana-opentelemetry-java.jar grafana-opentelemetry-java.jar

EXPOSE 8080
ENTRYPOINT ["sh", "-c", "exec java -javaagent:./grafana-opentelemetry-java.jar -jar ./app.jar"]