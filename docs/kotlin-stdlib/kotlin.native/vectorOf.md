

# vectorOf

Warning since 1.9

```kotlin
external fun vectorOf(f0: Float, f1: Float, f2: Float, f3: Float): Vector128(source)
```

```kotlin
import kotlin.native.vectorOf
import kotlin.native.vector.*

fun main() {
    // Create two 128‑bit vectors each holding four 32‑bit floating point values
    val v1 = vectorOf(1.0f, 2.0f, 3.0f, 4.0f)
    val v2 = vectorOf(5.0f, 6.0f, 7.0f, 8.0f)

    // Add the vectors element‑wise
    val sum = v1 + v2

    // Print the result
    println("Sum: $sum")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.native/vector-of.html)

    