

# ptr

Returns the pointer to this data or code.

```kotlin
val <T : CPointed> T.ptr: CPointer<T>(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() {
    // Allocate a C integer
    val intVar = alloc<IntVar>()
    intVar.value = 5

    // Get a CPointer to the integer using .ptr
    val intPtr: CPointer<IntVar> = intVar.ptr

    // Read the value through the pointer
    println("Value via pointer: ${intPtr.pointed.value}")

    // Modify the value through the pointer
    intPtr.pointed.value = 10
    println("Updated value in original: ${intVar.value}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/ptr.html)

    