

# toCStringArray

Convert this list of Kotlin strings to C array of C strings, allocating memory for the array and C strings with given AutofreeScope.

```kotlin
fun List<String>.toCStringArray(autofreeScope: AutofreeScope): CPointer<CPointerVar<ByteVar>>(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() {
    val strings = listOf("foo", "bar", "baz")

    // Convert Kotlin strings to a C array of C strings.
    val cArray: CPointer<CPointerVar<ByteVar>> = autofreeScope {
        strings.toCStringArray(this)
    }

    // Example: print each C string as a Kotlin string.
    for (i in 0 until strings.size) {
        println(cArray[i]?.toKString())
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/to-c-string-array.html)

    