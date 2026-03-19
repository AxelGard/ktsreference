

# reinterpret

Changes the interpretation of the pointed data or code.

```kotlin
inline fun <T : NativePointed> NativePointed.reinterpret(): T(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

fun main() = memScoped {
    // Allocate an Int and set its value
    val intPtr: CPointer<IntVar> = nativeHeap.alloc()
    intPtr.pointed.value = 0x12345678

    // Reinterpret the Int pointer as a Byte pointer
    val bytePtr: CPointer<ByteVar> = intPtr.reinterpret()

    // Print each byte of the original Int
    for (i in 0 until 4) {
        println("Byte $i: 0x${bytePtr[i].toUByte().toString(16)}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/reinterpret.html)

    