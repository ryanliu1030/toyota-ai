import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:toyota_ai/record.dart';
import 'pages/new_page.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const MaterialApp(
    title: 'Navigation Basics',
    home: MyApp(),
  ));
  SystemChrome.setEnabledSystemUIMode(SystemUiMode.manual, overlays: [
    SystemUiOverlay.top
  ]);
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
              child: Row(
                children: [
                  Transform.rotate(
                      angle: 90 * 3.1415926535 / 180,
                      child: Container(
                        width: 100,
                        height: 150,
                        child: RecordWidget(),
                      )
                  ),
                  // Transform.rotate(
                  //   angle: 90 * 3.1415926535 / 180,
                  //   child: ElevatedButton.icon(
                  //     style: ElevatedButton.styleFrom(
                  //       backgroundColor: Colors.black12,
                  //       foregroundColor: Colors.white,
                  //       fixedSize: const Size(120,50),
                  //     ),
                  //     onPressed: (){
                  //       // Handle Button press
                  //     },
                  //     icon: Icon(Icons.mic),
                  //     label: Text("Record"),
                  //   ),
                  // ),
                  Stack(
                    children: [
                      Transform.rotate(
                          angle: 90 * 3.1415926535 / 180,
                          child: Padding(
                            padding: EdgeInsets.all(20.0),
                            child: Image.asset(
                              "assets/images/Toyota_BZ4X.png",
                              width:700,
                              height:900,
                            ),
                          )
                      ),
                      Container(
                          height: 950,
                          width: 200,
                          decoration: const BoxDecoration(
                              color: Colors.black45,
                              borderRadius: BorderRadius.all(Radius.circular(20))
                          ),
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Transform.rotate(
                                angle: 90 * 3.1415926535 / 180,
                                child: ElevatedButton.icon(
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: Colors.black12,
                                    foregroundColor: Colors.white,
                                    fixedSize: const Size(150,150),
                                  ),
                                  onPressed: (){
                                    // Handle Button press
                                  },
                                  icon: Icon(Icons.star),
                                  label: Text("Favorites"),
                                ),
                              ),
                              const SizedBox(height: 60),
                              Transform.rotate(
                                angle: 90 * 3.1415926535 / 180,
                                child: ElevatedButton.icon(
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: Colors.black12,
                                    foregroundColor: Colors.white,
                                    fixedSize: const Size(150,150),
                                  ),
                                  onPressed: (){
                                    // Handle Button press
                                  },
                                  icon: Icon(Icons.directions_car),
                                  label: Text("Status"),
                                ),
                              ),
                              const SizedBox(height: 60),
                              Transform.rotate(
                                angle: 90 * 3.1415926535 / 180,
                                child: ElevatedButton.icon(
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: Colors.black12,
                                    foregroundColor: Colors.white,
                                    fixedSize: const Size(150,150),
                                  ),
                                  onPressed: (){
                                    // Handle Button press
                                  },
                                  icon: Icon(Icons.wind_power),
                                  label: Text("A/C"),
                                ),
                              ),
                              const SizedBox(height: 60),
                              Transform.rotate(
                                angle: 90 * 3.1415926535 / 180,
                                child: ElevatedButton.icon(
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: Colors.black12,
                                    foregroundColor: Colors.white,
                                    fixedSize: const Size(150,150),
                                  ),
                                  onPressed: (){
                                    Navigator.push(
                                      context,
                                      MaterialPageRoute(builder: (context) => NewPage()),
                                    );
                                  },
                                  icon: Icon(Icons.place),
                                  label: Text("Location"),
                                ),
                              ),
                            ],
                          )
                      )
                    ],
                  ),
                ],
              )
            )
        )
    );
  }
}