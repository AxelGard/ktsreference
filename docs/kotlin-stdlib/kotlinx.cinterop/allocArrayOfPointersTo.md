

# allocArrayOfPointersTo

Allocates C array of pointers to given elements.

```kotlin
fun <T : CPointed> NativePlacement.allocArrayOfPointersTo(elements: List<T?>): CArrayPointer<CPointerVar<T>>(source)
```

```kotlin
import kotlinx.cinterop.*
import platform.posix.*

fun main() {
    memScoped {
        // List of Kotlin strings, including a null element
        val kotlinStrings = listOf("hello", "world", null)

        // Convert each non‑null string to a C string pointer
        val cStringPointers: List<CPointer<ByteVar>?> =
            kotlinStrings.map { it?.toCStr() }

        // Allocate a C array of pointers to those C strings
        val array: CArrayPointer<CPointerVar<ByteVar>> =
            allocArrayOfPointersTo(cStringPointers)

        // Example: read back the first string from the C array
        val firstString = array[0]?.pointed?.toKString()
        println("First string: $firstString")  // prints: First string: hello
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/alloc-array-of-pointers-to.html)

    