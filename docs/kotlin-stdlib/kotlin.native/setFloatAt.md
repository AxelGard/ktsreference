

# setFloatAt

Sets Float out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.setFloatAt(index: Int, value: Float)(source)
```

```kotlin
import kotlin.native.ExperimentalNativeApi

@OptIn(ExperimentalNativeApi::class)
fun main() {
    // Create a byte array large enough for two Float values (4 bytes each)
    val buffer = ByteArray(8)

    // Store float values at specific indices
    buffer.setFloatAt(0, 1.23f)   // first 4 bytes
    buffer.setFloatAt(4, 4.56f)   // next 4 bytes

    // Read back the stored values
    println("Float at index 0: ${buffer.getFloatAt(0)}")   // 1.23
    println("Float at index 4: ${buffer.getFloatAt(4)}")   // 4.56
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-float-at.html)

    