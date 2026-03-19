

# compareValuesBy

Compares two values using the specified functions selectors to calculate the result of the comparison. The functions are called sequentially, receive the given values a and b and return Comparable objects. As soon as the Comparable instances returned by a function for a and b values do not compare as equal, the result of that comparison is returned.

```kotlin
fun <T> compareValuesBy(a: T, b: T, vararg selectors: (T) -> Comparable<*>?): Int(source)(source)
```

```kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val alice = Person("Alice", 30)
    val bob   = Person("Bob", 25)

    // Compare by age first, then by name
    val result = compareValuesBy(alice, bob,
        { it.age },
        { it.name })

    when {
        result < 0 -> println("alice comes before bob")
        result > 0 -> println("bob comes before alice")
        else       -> println("both are equal")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.comparisons/compare-values-by.html)

    