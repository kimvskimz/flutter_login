<?php
// 구글이 보낸 code 파라미터 받기
$code = $_GET['code'] ?? '';
if ($code) {
    // Streamlit 앱으로 다시 전달
    header("Location: https://flutterapp-4zjj2sg2jnpcbz4sfhpkee.streamlit.app/?code=" . urlencode($code));
    exit;
} else {
    echo "No code received.";
}
?>
