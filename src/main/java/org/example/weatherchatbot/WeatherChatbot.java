package org.example.weatherchatbot;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import org.json.JSONObject;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class WeatherChatbot extends Application {
    private VBox chatBox = new VBox(10);
    private TextField inputField = new TextField();

    @Override
    public void start(Stage primaryStage) {
        chatBox.setPadding(new Insets(10));
        chatBox.setStyle("-fx-background-color: #F0F0F0;");

        ScrollPane scrollPane = new ScrollPane(chatBox);
        scrollPane.setFitToWidth(true);
        scrollPane.setStyle("-fx-background: #F0F0F0; -fx-border-color: transparent;");

        inputField.setPromptText("Type a message...");
        inputField.setStyle("-fx-font-size: 14px; -fx-padding: 10px;");

        Button sendButton = new Button("Send");
        sendButton.setStyle("-fx-background-color: #FF0000; -fx-text-fill: white; -fx-font-size: 14px; -fx-padding: 5px 10px 7px 10px;");
        sendButton.setOnAction(e -> sendMessage());

        HBox inputBox = new HBox(10, inputField, sendButton);
        inputBox.setPadding(new Insets(10));
        HBox.setHgrow(inputField, Priority.ALWAYS);

        VBox root = new VBox(10, scrollPane, inputBox);
        VBox.setVgrow(scrollPane, Priority.ALWAYS); // Ensures chat messages expand while input stays at the bottom
        root.setStyle("-fx-background-color: #F0F0F0;");

        Scene scene = new Scene(root, 400, 500);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Chatbot");
        primaryStage.show();
    }

    private void sendMessage() {
        String userMessage = inputField.getText().trim();
        if (userMessage.isEmpty()) return;

        addMessage("You", userMessage, "#FF0000", "#FFFFFF", true); // Add user message to chatbox first
        inputField.clear();

        new Thread(() -> {
            String botReply = getBotResponse(userMessage);
            Platform.runLater(() -> addMessage("Bot", botReply, "#E5E5E5", "#000000", false));
        }).start();
    }

    private String getBotResponse(String message) {
        try {
            JSONObject json = new JSONObject();
            json.put("message", message);
            String jsonString = json.toString();

            URL url = new URL("http://127.0.0.1:8000/chatbot/");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json; utf-8");
            conn.setRequestProperty("Accept", "application/json");
            conn.setDoOutput(true);

            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            int responseCode = conn.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream(), "utf-8"))) {
                    StringBuilder response = new StringBuilder();
                    String line;
                    while ((line = reader.readLine()) != null) {
                        response.append(line);
                    }
                    JSONObject jsonResponse = new JSONObject(response.toString());
                    return jsonResponse.optString("response", "No response.");
                }
            } else {
                return "Error: Server returned status " + responseCode;
            }

        } catch (Exception e) {
            e.printStackTrace();
            return "Error: Unable to connect to server.";
        }
    }

    private void addMessage(String sender, String message, String bgColor, String textColor, boolean isUser) {
        Label messageLabel = new Label(message);
        messageLabel.setWrapText(true);
        messageLabel.setMaxWidth(300);
        messageLabel.setStyle(String.format("-fx-background-color: %s; -fx-text-fill: %s; -fx-padding: 10px; -fx-background-radius: 15px;", bgColor, textColor));

        HBox messageContainer = new HBox(messageLabel);
        messageContainer.setPadding(new Insets(5));

        if (isUser) {
            messageContainer.setStyle("-fx-alignment: center-right;");
        } else {
            messageContainer.setStyle("-fx-alignment: center-left;");
        }

        chatBox.getChildren().add(messageContainer);
    }

    public static void main(String[]args){
        launch(args);
    }
}
