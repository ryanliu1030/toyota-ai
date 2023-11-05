import 'package:permission_handler/permission_handler.dart';

permissionRequester() async {
  await Permission.location.request();
  await Permission.microphone.request();
}