

# initBy

Add @OverrideInit to constructor to make it override Objective-C initializer

```kotlin
external fun <T : ObjCObjectBase> T.initBy(constructorCall: T): T(source)
```

```kotlin
import platform.UIKit.*
import platform.Foundation.*

fun main() {
    // Create a UILabel by overriding its Objective‑C initializer
    val label = UILabel().initBy(
        UILabel().initWithFrame(CGRectMake(0.0, 0.0, 200.0, 50.0))
    )

    label.text = "Hello, world!"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/init-by.html)

    