

# plus

Concatenates this string with the string representation of the given other object. If either the receiver or the other object are null, they are represented as the string "null".

```kotlin
expect operator fun String?.plus(other: Any?): String(source)
```

```kotlin
fun main() {
    val greeting: String? = "Hello"
    val name: Any? = "World"
    println(greeting + name) // Prints: HelloWorld

    val nullString: String? = null
    val number: Any? = 42
    println(nullString + number) // Prints: null42

    val kotlinStr: String? = "Kotlin"
    val nullObj: Any? = null
    println(kotlinStr + nullObj) // Prints: Kotlinnull
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/plus.html)

    