FROM eclipse-temurin:22.0.2_9-jdk
COPY target/app.jar ./app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "./app.jar"]