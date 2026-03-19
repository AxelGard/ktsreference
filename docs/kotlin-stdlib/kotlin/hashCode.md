

# hashCode

Returns a hash code value for the object or zero if the object is null.

```kotlin
inline fun Any?.hashCode(): Int(source)
```

```kotlin
fun main() {
    val str: String? = "Kotlin"
    val nullable: String? = null

    println(str.hashCode())      // hash code of "Kotlin"
    println(nullable.hashCode()) // prints 0
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/hash-code.html)

    