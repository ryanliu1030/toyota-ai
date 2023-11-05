import 'package:flutter/material.dart';
import 'package:flutter_sound/flutter_sound.dart';
import 'package:path_provider/path_provider.dart';
import 'package:permission_handler/permission_handler.dart';

class RecordWidget extends StatefulWidget{
  @override
  State<RecordWidget> createState() => _RecordWidget();
}

class _RecordWidget extends State <RecordWidget> {
  final recorder = FlutterSoundRecorder();

  @override
  void initState() {
    super.initState();
    initRecorder();
  }

  @override
  void dispose() {
    recorder.closeRecorder();
    super.dispose();
  }

  Future initRecorder() async {
    final status = await Permission.microphone.request();
    if (status != PermissionStatus.granted){
      throw 'Microphone permission not granted';
    }
    await recorder.openRecorder();
  }

  Future record() async {
    final appDir = await getApplicationDocumentsDirectory();
    final filePath = '${appDir.path}/assets/recordings';
    await recorder.startRecorder(toFile: filePath);
  }

  Future stop() async {
    await recorder.stopRecorder();
  }

  @override
  Widget build (BuildContext context) => Scaffold(
    backgroundColor: Colors.grey.shade900,
    body: Center(
      child: ElevatedButton(
        child: Icon(
          recorder.isRecording ? Icons.stop : Icons.mic,
          size: 80,
        ),
        onPressed: () async {
          if (recorder.isRecording) {
            await stop();
          } else{
            await record();
          }
        },
      )
    ),
  );
}