

# narrow

Deprecated without replacement as part of the obsolete interop API

```kotlin
inline external fun <R : Number> Number.narrow(): R(source)
```

```kotlin
import kotlinx.cinterop.*

fun main() {
    val value: Double = 42.78

    // Narrow the Double to an Int
    val intVal: Int = value.narrow()

    // Narrow the same Double to a Long
    val longVal: Long = value.narrow()

    println("Int value: $intVal")   // Int value: 42
    println("Long value: $longVal") // Long value: 42
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlinx.cinterop/narrow.html)

    