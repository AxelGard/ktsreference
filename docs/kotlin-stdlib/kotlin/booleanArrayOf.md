

# booleanArrayOf

Returns an array containing the specified boolean values.

```kotlin
expect fun booleanArrayOf(vararg elements: Boolean): BooleanArray(source)
```

```kotlin
fun main() {
    // Create a BooleanArray with three elements
    val flags = booleanArrayOf(true, false, true)

    // Access elements
    println("First flag: ${flags[0]}")   // true
    println("Second flag: ${flags[1]}")  // false
    println("Third flag: ${flags[2]}")   // true

    // Iterate over the array
    flags.forEachIndexed { index, value ->
        println("flags[$index] = $value")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/boolean-array-of.html)

    