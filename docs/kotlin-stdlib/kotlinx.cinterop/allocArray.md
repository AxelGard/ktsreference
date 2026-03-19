

# allocArray

Allocates C array of given elements type and length.

```kotlin
inline fun <T : CVariable> NativePlacement.allocArray(length: Long): CArrayPointer<T>(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

fun main() = memScoped {
    // Allocate an array of 5 C integers
    val intArray: CArrayPointer<IntVar> = allocArray<IntVar>(5L)

    // Fill the array
    for (i in 0 until 5) {
        intArray[i] = i.toIntVar()
    }

    // Read and print the values
    for (i in 0 until 5) {
        println("intArray[$i] = ${intArray[i]}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/alloc-array.html)

    