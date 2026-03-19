

# interpretCPointer

Performs type cast of the CPointer from the given raw pointer.

```kotlin
external fun <T : CPointed> interpretCPointer(rawValue: NativePtr): CPointer<T>?(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

fun main() {
    // Allocate 4 bytes for an Int
    val raw: NativePtr = malloc(4) ?: error("malloc failed")

    // Interpret the raw pointer as a typed CPointer<IntVar>
    val intPtr = interpretCPointer<IntVar>(raw)

    // Write a value through the typed pointer
    intPtr?.pointed?.value = 42

    // Read the value back
    println(intPtr?.pointed?.value)  // prints 42

    // Free the memory
    free(raw)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/interpret-c-pointer.html)

    