import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.grey[850],
        body: Center(
          child: Stack(
            children: [
              Transform.rotate(
                angle: 90 * 3.1415926535 / 180,
                child: Image.asset(
                  "assets/images/Toyota_BZ4X.png",
                  width: 300,
                  height:300,
                ),
              ),
              Container(
                height: 900,
                width: 300,
                child: Text("Mitch KOKO"),
                decoration: const BoxDecoration(
                    color: Colors.black45,
                    borderRadius: BorderRadius.all(Radius.circular(20))
                ),
              )
            ],
          )
        )
      )
    );
  }
}