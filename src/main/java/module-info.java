module org.example.weatherchatbot {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;
    requires java.net.http;
    requires org.json;

    opens org.example.weatherchatbot to javafx.fxml;
    exports org.example.weatherchatbot;
}