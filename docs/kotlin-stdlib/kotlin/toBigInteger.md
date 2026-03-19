

# toBigInteger

Returns the value of this Int number as a BigInteger.

```kotlin
inline fun Int.toBigInteger(): BigInteger(source)
```

```kotlin
import java.math.BigInteger

fun main() {
    val smallNumber: Int = 123456
    val bigInt: BigInteger = smallNumber.toBigInteger()
    val doubled = bigInt * 2.toBigInteger()

    println("Small: $smallNumber")
    println("Big: $bigInt")
    println("Doubled: $doubled")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/to-big-integer.html)

    