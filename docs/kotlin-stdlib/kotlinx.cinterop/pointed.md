

# pointed

Returns the corresponding CPointed.

```kotlin
val <T : CPointed> CPointer<T>.pointed: T(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

fun main() = memScoped {
    // Allocate an array of 5 CInt elements
    val ptr: CPointer<CInt> = allocArray(5)

    // Use the `pointed` property to get a CArrayVar view
    val array = ptr.pointed

    // Set values via the array view
    array[0] = 10
    array[1] = 20
    array[2] = 30

    // Read and print the values
    println("array[0] = ${array[0]}")
    println("array[1] = ${array[1]}")
    println("array[2] = ${array[2]}")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/pointed.html)

    