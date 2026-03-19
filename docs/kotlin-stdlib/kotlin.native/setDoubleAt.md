

# setDoubleAt

Sets Double out of the ByteArray byte buffer at specified index index

```kotlin
@ExperimentalNativeApiexternal fun ByteArray.setDoubleAt(index: Int, value: Double)(source)
```

```kotlin
@OptIn(ExperimentalNativeApi::class)
fun main() {
    // Create a byte buffer large enough for two Double values (16 bytes)
    val buffer = ByteArray(16)

    // Store two double values at positions 0 and 8
    buffer.setDoubleAt(0, 3.14159)   // first double
    buffer.setDoubleAt(8, 2.71828)   // second double

    // The buffer now contains the binary representation of the doubles
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/set-double-at.html)

    