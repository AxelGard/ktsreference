

# compareTo

Compares two strings lexicographically, optionally ignoring case differences.

```kotlin
expect fun String.compareTo(other: String, ignoreCase: Boolean = false): Int(source)
```

```kotlin
fun main() {
    val first = "apple"
    val second = "banana"

    // Compare two strings lexicographically
    val lexResult = first.compareTo(second)
    println("Comparing \"$first\" to \"$second\": $lexResult")
    // Output will be a negative number because "apple" comes before "banana"

    val third = "Apple"

    // Compare ignoring case differences
    val ignoreCaseResult = first.compareTo(third, ignoreCase = true)
    println("Comparing \"$first\" to \"$third\" ignoring case: $ignoreCaseResult")
    // Output will be 0 because they are equal ignoring case
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/compare-to.html)

    