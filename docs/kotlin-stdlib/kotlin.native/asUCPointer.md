

# asUCPointer

Warning since 1.9

```kotlin
fun ImmutableBlob.asUCPointer(offset: Int = 0): CPointer<UByteVar>(source)
```

```kotlin
import kotlinx.cinterop.*
import kotlin.native.concurrent.*

fun main() {
    // Create an ImmutableBlob from a byte array
    val bytes = byteArrayOf(10, 20, 30, 40, 50)
    val blob = ImmutableBlob(bytes)

    // Obtain a CPointer<UByteVar> pointing to the start of the blob
    val ptr: CPointer<UByteVar> = blob.asUCPointer()

    // Read values through the pointer (indices are 0‑based)
    println("First byte: ${ptr[0]}")   // 10
    println("Last byte:  ${ptr[4]}")   // 50

    // Obtain a pointer with an offset (skip the first two bytes)
    val offsetPtr: CPointer<UByteVar> = blob.asUCPointer(offset = 2)
    println("Byte at offset 2: ${offsetPtr[0]}") // 30
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/as-u-c-pointer.html)

    