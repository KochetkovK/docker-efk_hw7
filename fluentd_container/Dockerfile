FROM fluent/fluentd:v1.12.0-debian-1.0
USER root
RUN ["gem", "install", "elasticsearch", "--no-document", "--version", "7.13.1"]
RUN ["gem", "install", "excon", "-v", "0.109.0"]
RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-document", "--version", "5.0.5"]
RUN ["gem", "install", "fluent-plugin-grok-parser", "--no-document"]
USER fluent