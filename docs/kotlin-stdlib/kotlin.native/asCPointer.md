

# asCPointer

Warning since 1.9

```kotlin
fun ImmutableBlob.asCPointer(offset: Int = 0): CPointer<ByteVar>(source)
```

```kotlin
import kotlin.native.memory.ImmutableBlob
import kotlinx.cinterop.*

fun main() {
    // Create a byte array and wrap it in an ImmutableBlob
    val data = "Hello, Kotlin!".toByteArray()
    val blob = ImmutableBlob(data)

    // Obtain a C pointer to the start of the blob
    val ptr: CPointer<ByteVar> = blob.asCPointer()

    // Access bytes via the C pointer
    println("First byte: ${ptr[0]}")          // prints 72 ('H')
    println("Fourth byte: ${ptr[3]}")         // prints 111 ('o')

    // Get a pointer with an offset (skip first 7 bytes)
    val offsetPtr = blob.asCPointer(7)
    println("Offset string: ${offsetPtr.reinterpret<CCharVar>().toKString()}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/as-c-pointer.html)

    