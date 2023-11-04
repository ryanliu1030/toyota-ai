import 'package:flutter/material.dart';

class Test_Name extends StatelessWidget {
  const Test_Name({Key? home}) : super(key: home);

  @override
  Widget build(BuildContext context) {
    return Test_Name(
        home: Scaffold(
            body: SingleChildScrollView(
              child: Center(
                child: Container(
                  width: 200,
                  height: 200,
                  decoration: BoxDecoration(
                    color: Colors.blue,
                    borderRadius: BorderRadius.circular(12.0),
                  ),
                )
              )
            )
        )
    );
  }
}