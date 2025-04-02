module org.example.weatherchatbot {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;

    opens org.example.weatherchatbot to javafx.fxml;
    exports org.example.weatherchatbot;
}