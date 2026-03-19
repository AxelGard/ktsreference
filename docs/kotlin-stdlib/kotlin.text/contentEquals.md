

# contentEquals

Returns true if the contents of this char sequence are equal to the contents of the specified other, i.e. both char sequences contain the same number of the same characters in the same order.

```kotlin
expect infix fun CharSequence?.contentEquals(other: CharSequence?): Boolean(source)
```

```kotlin
fun main() {
    val text: CharSequence? = "kotlin"
    val builder: CharSequence? = StringBuilder("kotlin")

    val areEqual = text contentEquals builder
    println("Sequences are equal: $areEqual")   // Prints: Sequences are equal: true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/content-equals.html)

    